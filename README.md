# Smart City Control Center

A Python project simulating a smart-building monitoring system.
Built as a learning project. **All data is simulated; no physical hardware is used.**

## What it does
- Tracks multiple sensor types (temperature, occupancy, energy, humidity)
- Classifies each reading as normal, alert, or critical
- Flags unknown sensor types instead of ignoring them
- Prints a summary listing which sensors need attention

## Run it
```
python building_monitor.py
```

## Example output
```
Lobby: 72 °F - Status: normal
Server Room: 55 °F - ALERT: too cold
Floor 3: 51 people - ALERT: over capacity
Roof: 104 °F - CRITICAL: evacuate zone
HVAC Unit: 60 kW - ALERT: high energy use
Lab: 45 % - Status: normal
6 sensors checked.
4 in alert or critical state.
Needs attention: Server Room, Floor 3, Roof, HVAC Unit
4 in alert or critical state.
Needs attention: Server Room, Floor 3, Roof, HVAC Unit
```

## Roadmap
- [x] Week 1: sensor classification, functions, dictionaries
- [ ] Week 2: read sensor data from JSON files, add a dashboard
- [ ] Later: MQTT messaging, Streamlit dashboard, optional ESP32 hardware