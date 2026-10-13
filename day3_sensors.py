readings = [72, 68, 91, 55, 104, 77]
names = ["Lobby", "Floor 2", "Floor 3", "Server Room", "Roof", "Garage"]

for name, temp in zip(names, readings):
    if temp > 100:
        print(f"{name}: {temp} -  CRITICAL: evacuate zone")
    elif temp >= 85:
        print(f"{name}: {temp} - ALERT: too hot")
    elif temp <= 60:
        print(f"{name}: {temp} - ALERT: too cold")
    else:
        print(f"{name}: {temp} - Status: normal")

print(f"{len(readings)} readings checked.")
bad_readings = 0
for temp in readings:
    if temp <= 60 or temp >= 85:
        bad_readings += 1
print(bad_readings)
print(max(readings))