# Shelly 1PM Exporter

Containerized Prometheus Exporter for [Shelly 1PM](https://shelly.cloud/products/shelly-1pm-smart-home-automation-relay/)


### Run

```
export TARGETS=192.168.1.110,192.168.1.21
flask run --host=0.0.0.0
```


### Develop

```
TARGETS=192.168.1.110 docker-compose up
```

### Sample Metrics

```
# HELP shelly_1pm_max_power Power threshold above which an overpower condition will be triggered
# TYPE shelly_1pm_max_power gauge
shelly_1pm_max_power{device_type="SHSW-PM",device_name="My Device",device_serial_number="3692",device_hostname="shelly1pm-8CAAB55F31AF",device_mac="8CAAB55F31AF",device_ip="192.168.1.110",device_build_id="20220209-094317/v1.11.8-g8c7bb8d",device_hw_revision="prod-191219"} 1800
# HELP shelly_1pm_update_available Indicates an update is available
# TYPE shelly_1pm_update_available gauge
shelly_1pm_update_available{device_type="SHSW-PM",device_name="Rack Outlet",device_serial_number="3692",device_hostname="shelly1pm-8CAAB55F31AF",device_mac="8CAAB55F31AF",device_ip="192.168.1.110",device_build_id="20220209-094317/v1.11.8-g8c7bb8d",device_hw_revision="prod-191219"} 0
# HELP shelly_1pm_rssi Wifi signal strength
# TYPE shelly_1pm_rssi gauge
shelly_1pm_rssi{device_type="SHSW-PM",device_name="Rack Outlet",device_serial_number="3692",device_hostname="shelly1pm-8CAAB55F31AF",device_mac="8CAAB55F31AF",device_ip="192.168.1.110",device_build_id="20220209-094317/v1.11.8-g8c7bb8d",device_hw_revision="prod-191219"} -64
# HELP shelly_1pm_device_temperature Internal device temperature in Celcius
# TYPE shelly_1pm_device_temperature gauge
shelly_1pm_device_temperature{device_type="SHSW-PM",device_name="Rack Outlet",device_serial_number="3692",device_hostname="shelly1pm-8CAAB55F31AF",device_mac="8CAAB55F31AF",device_ip="192.168.1.110",device_build_id="20220209-094317/v1.11.8-g8c7bb8d",device_hw_revision="prod-191219"} 37.19
# HELP shelly_1pm_device_overtemperature Indicates device has overheated
# TYPE shelly_1pm_device_overtemperature gauge
shelly_1pm_device_overtemperature{device_type="SHSW-PM",device_name="Rack Outlet",device_serial_number="3692",device_hostname="shelly1pm-8CAAB55F31AF",device_mac="8CAAB55F31AF",device_ip="192.168.1.110",device_build_id="20220209-094317/v1.11.8-g8c7bb8d",device_hw_revision="prod-191219"} 0
# HELP shelly_1pm_power Current real AC power being drawn, in Watts
# TYPE shelly_1pm_power gauge
shelly_1pm_power{device_type="SHSW-PM",device_name="Rack Outlet",device_serial_number="3692",device_hostname="shelly1pm-8CAAB55F31AF",device_mac="8CAAB55F31AF",device_ip="192.168.1.110",device_build_id="20220209-094317/v1.11.8-g8c7bb8d",device_hw_revision="prod-191219"} 0.0
# HELP shelly_1pm_avg_power_3m Average real AC power being drawn over last 3 minute window, in Watts
# TYPE shelly_1pm_avg_power_3m gauge
shelly_1pm_avg_power_3m{device_type="SHSW-PM",device_name="Rack Outlet",device_serial_number="3692",device_hostname="shelly1pm-8CAAB55F31AF",device_mac="8CAAB55F31AF",device_ip="192.168.1.110",device_build_id="20220209-094317/v1.11.8-g8c7bb8d",device_hw_revision="prod-191219"} 0.0
# HELP shelly_1pm_total_power Total energy consumed by the attached electrical appliance in Watt-hour
# TYPE shelly_1pm_total_power counter
shelly_1pm_total_power{device_type="SHSW-PM",device_name="Rack Outlet",device_serial_number="3692",device_hostname="shelly1pm-8CAAB55F31AF",device_mac="8CAAB55F31AF",device_ip="192.168.1.110",device_build_id="20220209-094317/v1.11.8-g8c7bb8d",device_hw_revision="prod-191219"} 0.0
```
