def classify_temperature(temp):
    if temp > 100:
        return "CRITICAL: evacuate zone"
    elif temp >= 85:
        return "ALERT: too hot"
    elif temp <= 60:
        return "ALERT: too cold"
    else:
        return "Status: normal"

def summarize(names, readings, bad_readings):
    if readings:
        print(f"{len(readings)} readings checked.")
        print(f"{bad_readings} readings in alert or critical state.")
        print(f"Highest reading: {max(readings)}")
    else:
        print("No readings received - check sensor connection.")

readings = [72, 68, 91, 55, 104, 77]
names = ["Lobby", "Floor 2", "Floor 3", "Server Room", "Roof", "Garage"]

bad_readings = 0
for name, temp in zip(names, readings):
    status = classify_temperature(temp)
    print(f"{name}: {temp} - {status}")
    if not status.startswith("Status"):
        bad_readings += 1
summarize(names, readings, bad_readings)

