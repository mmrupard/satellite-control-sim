import requests
import csv
from datetime import datetime
from db import init_db, save_telemetry

init_db()

def get_telemetry():
    url = "http://localhost:5001/get_telemetry"
    response = requests.get(url)
    data = response.json()

    timestamp = datetime.now()
    voltage = data["battery_voltage"]
    temperature = data["temperature"]
    status = data["payload_status"]

    #TODO: this can removed whenever
    log_telemetry(data)

    save_telemetry(timestamp, voltage, temperature, status)
    return data

def log_telemetry(data):
    with open("data/telemetry_log.csv", mode="a+") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), data["battery_voltage"], data["temperature"], data["payload_status"]])