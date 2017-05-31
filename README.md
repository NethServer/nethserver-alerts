# nethserver-alerts

Route collectd notifications to my.nethesis.it
Configure collectd thresholds to trigger notifications when alert events occurs

## Trigge an alarm from command line

Example here:

```
#!/bin/bash
# Exec passed arguments as command
$@

# Check exit status
if [[ $? != 0 ]] ; then
    # Alert if command failed
    echo -e "PUTNOTIF host=$(hostname) type=custom type_instance=$1 severity=failure time=$(date +%s) message=\"$1 FAILURE\"" | nc -U /var/run/collectd.sock &>/dev/null
else
    # Switch off alert if command succeed
    echo -e "PUTNOTIF host=$(hostname) type=custom type_instance=$1 severity=okay time=$(date +%s) message=\"$1 OK\"" | nc -U /var/run/collectd.sock &>/dev/null
fi

```

## How to add a threshold configuration

Create a /etc/collectd.d/threshold.conf template fragment using collectd threshold syntax. Enjoy collectd docs here https://collectd.org/documentation/manpages/collectd-threshold.5.shtml

