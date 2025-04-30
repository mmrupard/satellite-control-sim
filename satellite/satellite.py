import time
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

telemetry_data = {
    "battery_voltage": 12.5,
    "temperature": 35.0,
    "payload_status": "inactive"
}

@app.route("/send_command", methods=["POST"])
def receive_command():
    command = request.json.get("command", "none")
    print(f"Received command: {command}")

    if command == "activate_payload":
        telemetry_data["payload_status"] = "active"
    elif command == "deactivate_payload":
        telemetry_data["payload_status"] = "inactive"
    elif command == "adjust_power":
        telemetry_data["battery_voltage"] = round(random.uniform(11.5, 13.0), 2)
    else:
        print(f"Invalid Command: {command}")

    return jsonify({"status": "Command received"}), 200

@app.route("/get_telemetry", methods=["GET"])
def send_telemetry():
    telemetry_data["temperature"] = round(random.uniform(30.0, 40.0), 2)
    return jsonify(telemetry_data)

if __name__ == "__main__":
    app.run(port=5001)