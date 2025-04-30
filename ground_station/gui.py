import tkinter as tk
from command_center import send_command
from telemetry_listener import get_telemetry

def update_telemetry():
    data = get_telemetry()
    telemetry_text.set(f"Voltage: {data['battery_voltage']} V\n"
                       f"Temp: {data['temperature']} C\n"
                       f"Payload: {data['payload_status']}")
    root.after(3000, update_telemetry)

root = tk.Tk()
root.title("Ground Station Control")

telemetry_text = tk.StringVar()
tk.Label(root, textvariable=telemetry_text, font=("Helvetica", 14)).pack(pady=10)

tk.Button(root, text="Activate Payload", command=lambda: send_command("activate_payload")).pack()
tk.Button(root, text="Deactivate Payload", command=lambda: send_command("deactivate_payload")).pack()
tk.Button(root, text="Ajust Power", command=lambda: send_command("adjust_power")).pack()

update_telemetry()
root.mainloop()