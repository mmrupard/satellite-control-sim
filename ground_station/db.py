import sqlite3

DB_NAME = "data/telemetry.db"

def init_db():
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS telemetry (
            timestamp TEXT,
            battery_voltage REAL,
            temperature REAL,
            payload_status TEXT)
        """)
    connection.commit()
    connection.close()

def save_telemetry(timestamp, voltage, temperature, status):
    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO telemetry (timestamp, battery_voltage, temperature, payload_status)
        VALUES (?, ?, ? , ?)
    """, (timestamp, voltage, temperature, status))
    connection.commit()
    connection.close()
