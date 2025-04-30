import requests
import csv
from datetime import datetime

def get_telemetry():
    url = "http://localhost:5001/get_telemetry"
    response = requests.get(url)
    data = response.json()
    log_telemetry(data)
    return data

def log_telemetry(data):
    with open("data/telemetry_log.csv", mode="a+") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), data["battery_voltage"], data["temperature"], data["payload_status"]])