import requests
import csv
from datetime import datetime

def send_command(command):
    url = "http://localhost:5001/send_command"
    response = requests.post(url, json={"command": command})
    log_command(command)
    print(f"Sent command: {command} - Status: {response.status_code}")

def log_command(command):
    with open("data/command_log.csv", mode="a+") as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), command])