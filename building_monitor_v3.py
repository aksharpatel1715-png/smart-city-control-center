import json
import sys


def load_sensors(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERROR: sensor file '{path}' not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"ERROR: '{path}' is not valid JSON (line {e.lineno}, column {e.colno}): {e.msg}")
        return []


def load_config(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERROR: config file '{path}' not found. Cannot run without alarm limits.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: '{path}' is not valid JSON (line {e.lineno}, column {e.colno}): {e.msg}")
        sys.exit(1)


def is_valid_sensor(sensor):
    if not isinstance(sensor, dict):
        return False
    for key in ["name", "type", "value", "unit"]:
        if key not in sensor:
            return False
    if not isinstance(sensor["value"], (int, float)):
        return False
    return True


def classify_temperature(temp, limits):
    if temp > limits["critical_above"]:
        return "CRITICAL: evacuate zone"
    elif temp >= limits["hot_at_or_above"]:
        return "ALERT: too hot"
    elif temp <= limits["cold_at_or_below"]:
        return "ALERT: too cold"
    else:
        return "Status: normal"


def classify_occupancy(count, limits):
    if count > limits["max_people"]:
        return "ALERT: over capacity"
    else:
        return "Status: normal"


def classify_energy(kw, limits):
    if kw > limits["max_kw"]:
        return "ALERT: high energy use"
    else:
        return "Status: normal"


def classify_humidity(percent, limits):
    if percent > limits["max_percent"]:
        return "ALERT: too humid"
    elif percent < limits["min_percent"]:
        return "ALERT: too dry"
    else:
        return "Status: normal"


def classify_sensor(sensor, config):
    if sensor["type"] == "temperature":
        return classify_temperature(sensor["value"], config["temperature"])
    elif sensor["type"] == "occupancy":
        return classify_occupancy(sensor["value"], config["occupancy"])
    elif sensor["type"] == "energy":
        return classify_energy(sensor["value"], config["energy"])
    elif sensor["type"] == "humidity":
        return classify_humidity(sensor["value"], config["humidity"])
    else:
        return "ALERT: unknown sensor type"


def summarize(sensors, bad_count, bad_names):
    if sensors:
        print(f"{len(sensors)} sensors checked.")
        print(f"{bad_count} in alert or critical state.")
        if bad_names:
            print("Needs attention:", ", ".join(bad_names))
    else:
        print("No readings received - check sensor connection.")


config = load_config("config.json")
sensors = load_sensors("sensors.json")

bad_count = 0
bad_names = []

for sensor in sensors:
    if not is_valid_sensor(sensor):
        sensor_name = "Unknown sensor"
        if isinstance(sensor, dict):
            sensor_name = sensor.get("name", "Unknown sensor")
        print(f"{sensor_name}: ALERT: invalid reading")
        bad_count += 1
        bad_names.append(sensor_name)
        continue
    status = classify_sensor(sensor, config)
    print(f"{sensor['name']}: {sensor['value']} {sensor['unit']} - {status}")
    if not status.startswith("Status"):
        bad_count += 1
        bad_names.append(sensor["name"])

summarize(sensors, bad_count, bad_names)