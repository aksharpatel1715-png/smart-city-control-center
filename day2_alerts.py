temperature = int(input("Enter the temperature in °F: "))

if 100 > temperature > 85:
    print("ALERT: too hot")
elif temperature < 60:
    print("ALERT: too cold")
else:
    print("Status: normal")