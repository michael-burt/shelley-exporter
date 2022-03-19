import os

import requests
from flask import Flask, Response, jsonify

app = Flask(__name__)


def get_targets():
    return [target for target in os.getenv("TARGETS", "").split(",") if target != '']


def get_tags_str(tag_dict):
    return "{" + ",".join([f'{k}="{v}"' for k, v in tag_dict.items()]) + "}"


def get_1pm_data(target):
    settings_response = requests.get(f"http://{target}/settings")
    resp_obj = settings_response.json()

    status_response = requests.get(f"http://{target}/status")
    status_resp_obj = status_response.json()

    device = resp_obj.get("device", {})
    wifi_sta = status_resp_obj.get("wifi_sta", {})

    meters = status_resp_obj.get("meters", [{}])[0]

    labels = dict(
        device_type=device.get("type"),
        device_name=resp_obj.get("name"),
        device_hostname=device.get("hostname"),
        device_mac=device.get("mac"),
        device_ip=wifi_sta.get("ip"),
        device_build_id=resp_obj.get("build_info", {}).get("build_id"),
        device_hw_revision=resp_obj.get("hwinfo", {}).get("hw_revision"),
    )

    metrics = dict(
        max_power=(
            "gauge",
            "Power threshold above which an overpower condition will be triggered",
            resp_obj.get("max_power"),
        ),
        update_available=(
            "gauge",
            "Indicates an update is available",
            int(status_resp_obj.get("has_update")),
        ),
        rssi=(
            "gauge",
            "Wifi signal strength",
            wifi_sta.get("rssi"),
        ),
        device_temperature=(
            "gauge",
            "Internal device temperature in Celcius",
            status_resp_obj.get("temperature"),
        ),
        device_overtemperature=(
            "gauge",
            "Indicates device has overheated",
            int(status_resp_obj.get("overtemperature")),
        ),
        power=(
            "gauge",
            "Current real AC power being drawn, in Watts",
            meters.get("power"),
        ),
        avg_power_3m=(
            "gauge",
            "Average real AC power being drawn over last 3 minute window, in Watts",
            sum(meters.get("counters", [])),
        ),
        total_power=(
            "counter",
            "Total energy consumed by the attached electrical appliance in Watt-hour",
            meters.get("total", 0) / 60,
        ),
    )

    return dict(
        labels=labels,
        metrics=metrics,
    )


@app.route("/healthz", methods=["GET"])
def healthz():
    return jsonify({"status": "up"})


@app.route("/metrics", methods=["GET"])
def get_metrics():

    metrics = ""
    for target in get_targets():
        target_metadata = get_1pm_data(target)
        label_string = get_tags_str(target_metadata.get("labels", {}))

        for metric, value in target_metadata.get("metrics", {}).items():
            metrics += f"# HELP shelly_1pm_{metric} {value[1]}\n"
            metrics += f"# TYPE shelly_1pm_{metric} {value[0]}\n"
            metrics += f"shelly_1pm_{metric}{label_string} {value[2]}\n"

    return Response(metrics, mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=False)
