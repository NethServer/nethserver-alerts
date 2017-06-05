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


## Alerts DB default configuration

```
1=load
    DataSource=midterm
    FailureMax=10
    Hysteresis=3
    WarningMax=5
    Hits=3
2=df
    FailureMin=15
    Hysteresis=2
*   Instance=boot
    TypeInstance=free
3=df
    FailureMin=16
    Hysteresis=3
    Instance=root
    TypeInstance=free
4=swap
    FailureMin=10
    Hysteresis=1
    TypeInstance=free
5=uptime
    FailureMin=600
6=md
    FailureMax=0.1
    TypeInstance=failed
7=md
    FailureMax=0.1
*   TypeInstance=missing
8=lsm
    FailureMax=0.1
    TypeInstance=down
9=ping
    FailureMax=200
*   Instance=8.8.8.8
*   PluginType=ping
10=ping
    FailureMax=0.1
*   Instance=8.8.4.4
*   PluginType=ping_droprate
11=nut-ups
    FailureMin=300
    Instance=73.nethest.xxx
    PluginType=voltage
    TypeInstance=input

* Mandatory
```
