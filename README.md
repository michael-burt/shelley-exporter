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
