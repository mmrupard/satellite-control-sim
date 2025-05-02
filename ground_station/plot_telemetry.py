import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

DB_NAME = "data/telemetry.db"

def fetch_telemetry(n):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        SELECT timestamp, battery_voltage, temperature FROM telemetry
        ORDER BY timestamp DESC LIMIT ?
    """, (n,))

    rows = cursor.fetchall()
    connection.close()

    return rows[::-1]

def plot_telemetry(rows):
    timestamps = [row[0] for row in rows]
    voltages = [row[1] for row in rows]
    temperatures = [row[2] for row in rows]

    plt.figure(figsize=(10,5))
    plt.subplot(2, 1, 1)
    plt.plot(timestamps, voltages, label="Battery Voltage (V)", color='blue')
    plt.ylabel("Voltage (V)")
    plt.grid(True)
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(timestamps, temperatures, label="Temperature (C)", color='red')
    plt.ylabel("Temperature (C)")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    rows = fetch_telemetry(100)
    if rows:
        plot_telemetry(rows)
    else:
        print("No telemetry found.")