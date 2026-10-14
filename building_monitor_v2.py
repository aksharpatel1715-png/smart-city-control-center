import json
with open("sensors.json", encoding="utf-8") as f:
    sensors = json.load(f)

def classify_humidity(percent):
    if percent > 60:
        return "ALERT: too humid"
    elif percent < 30:
        return "ALERT: too dry"
    else:
        return "Status: normal"

def classify_temperature(temp):
    if temp > 100:
        return "CRITICAL: evacuate zone"
    elif temp >= 85:
        return "ALERT: too hot"
    elif temp <= 60:
        return "ALERT: too cold"
    else:
        return "Status: normal"


def classify_occupancy(count):
    if count > 50:
        return "ALERT: over capacity"
    else:
        return "Status: normal"


def classify_energy(kw):
    if kw > 50:
        return "ALERT: high energy use"
    else:
        return "Status: normal"


def classify_sensor(sensor):
    if sensor["type"] == "temperature":
        return classify_temperature(sensor["value"])
    elif sensor["type"] == "occupancy":
        return classify_occupancy(sensor["value"])
    elif sensor["type"] == "energy":
        return classify_energy(sensor["value"])
    elif sensor["type"] == "humidity":
        return classify_humidity(sensor["value"])
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


bad_count = 0
bad_names = []

for sensor in sensors:
    status = classify_sensor(sensor)
    print(f"{sensor['name']}: {sensor['value']} {sensor['unit']} - {status}")
    if not status.startswith("Status"):
        bad_count += 1
        bad_names.append(sensor["name"])

summarize(sensors, bad_count, bad_names)