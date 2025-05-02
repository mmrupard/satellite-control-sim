from flask import Flask, request
from flask_socketio import SocketIO, emit
import asyncio
import random
import time
import threading

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

async def telemetry_emitter():
    while True:
        data = {
            "temperature": round(random.uniform(20.0, 30.0), 2),
            "battery_voltage": round(random.uniform(3.0, 5.0), 2),
            "payload_status": "inactive"
        }
        await socketio.emit("telemetry", data)
        await asyncio.sleep(2) 
    
@socketio.on("connect")
async def handle_connect():
    print("Client connected")

@socketio.on("send_command")
async def handle_command(command):
    print(f"Received command: {command}")
    await socketio.emit("command_acknowledged", {"command": command})

@app.before_first_request
def start_background_task():
    socketio.start_background_task(telemetry_emitter)

if __name__ == '__main__':
   socketio.run(app, host="0.0.0.0", port=5000)