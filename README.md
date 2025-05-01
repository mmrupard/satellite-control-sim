# Simulated Satellite Command & Control System

A Python-based simulation of a ground station sending commands to a virtual satellite and receiving telemetry updates.

## Features

- GUI command interface (Tkinter)
- REST API between ground and satellite
- Simulated telemetry (temperature, voltage, payload)
- Command + telemetry logging (CSV)

## How to Run

Note: This currently only works if you run the server and gui from the root directory

1. Start the simulated satellite server:
   ```bash
   python satellite/satellite.py
   ```
2. Start the GUI
   ```bash
   python ground_station/gui.py
   ```

## TODO

- Add WebSocket support
- Replace GUI with Flask/React dashboard
- Store data in SQLite
- Add CCSDS-style packet structure
- Add Grafana displays
- Dockerize components
