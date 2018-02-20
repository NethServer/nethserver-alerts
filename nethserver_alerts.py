#
# Copyright (C) 2015 Nethesis S.r.l.
#
# All rights reserved.
#
# http://www.nethesis.it - info@nethesis.it
#

import collectd
import json
import requests
import time
import os
import threading

api_url = ""
lk = False
debug = False
HEARTBEAT_PERIOD = 600 # seconds
MAX_QUEUE_LENGTH = 50
NOTIF_FAILURE = 1
NOTIF_WARNING = 2
NOTIF_OKAY = 4


def dispatch(endpoint, payload):

    if endpoint and payload:
        dispatch.queue.append((endpoint, payload))

    if not dispatch.lock.acquire(False):
        return

    if len(dispatch.queue) > MAX_QUEUE_LENGTH:
        collectd.error("Queue is full. %s message(s) discarded, %s retained." % len(dispatch.queue[20:]), len(dispatch.queue))
        del dispatch.queue[0:len(dispatch.queue) - MAX_QUEUE_LENGTH]

    while len(dispatch.queue) > 0:
        endpoint, payload = dispatch.queue[0]
        try:
            response = requests.post(api_url + endpoint , payload, timeout = 20)
            if debug: collectd.info("[%s/%s] [%s] %s" % (response.status_code, response.reason, endpoint, json.dumps(payload)))
            if(response.status_code < 500):
                dispatch.queue.pop(0)
        except Exception as e:
            collectd.error("%s: %s" % (endpoint, str(e)))
            break

    dispatch.lock.release()

# "static" variables for dispatch() function:
dispatch.lock = threading.Lock()
dispatch.queue = []


def config(conf):
    global lk, api_url, debug
    for child in conf.children:
        if child.key == 'api_url':
            api_url = child.values[0]
            if not api_url.endswith("/"):
                api_url += "/"
        elif child.key == 'lk':
            lk = child.values[0]
        elif child.key == 'debug':
            debug = str(child.values[0]).lower() in ["1", "yes", "true", "enabled"]


def notify(n):
    if lk:
        p = {}
        p['lk'] = lk
        p['alert_id'] = ':'.join(filter(lambda x: isinstance(x, basestring) and bool(x), [n.plugin, n.plugin_instance, n.type, n.type_instance]))
        if n.severity == NOTIF_FAILURE:
            p['status'] = "FAILURE"
        elif n.severity == NOTIF_WARNING:
            p['status'] = "WARNING"
        elif n.severity == NOTIF_OKAY:
            p['status'] = "OK"

        p['message'] = n.message

        collectd.notice("[{status}] {alert_id}: {message}".format(**p))
        dispatch('alerts/store', p)


def heartbeat():
    endpoint = 'heartbeats/store'
    if lk:
        payload = {}
        payload['lk'] = lk

        try:
            response = requests.post(api_url + endpoint, payload, timeout = 20)
            if debug: collectd.info("[%s/%s] [%s] %s" % (response.status_code, response.reason, endpoint, response.json()))
        except Exception as e:
            collectd.error("%s: %s" % (endpoint, str(e)))

    # Try to dispatch pending messages
    dispatch(False, False)


def collectd_init():
    if lk:
        p = {}
        p['lk'] = lk
        p['status'] = "INIT"
        p['message'] = "NethServer ISA init"
        dispatch('alerts/store', p)


#
# collectd callbacks
#

collectd.register_config(config)
collectd.register_notification(notify)
collectd.register_init(collectd_init)
collectd.register_read(heartbeat, HEARTBEAT_PERIOD)

