from config.celery import celery

from celery import shared_task
from influxdb import InfluxDBClient
import random

from monitoring.departments.models import Department
from monitoring.sensors.models import Sensor

influxdb_host = "influxdb"
influxdb_port = 8086
influxdb_database = "sensors"

client = InfluxDBClient(host=influxdb_host, port=influxdb_port)
if influxdb_database not in client.get_list_database():
    client.create_database(influxdb_database)
client.switch_database(influxdb_database)


@shared_task
def generate_sensor_data():
    department = Department.objects.order_by("?").first()
    sensor = Sensor.objects.create(
        name=f"sensor-{random.randint(1, 5)}",
        temperature=round(random.uniform(18.0, 30.0), 2),
        oxygen_level=round(random.uniform(90.0, 100.0), 2),
        department=department,
    )

    sensor_data = {
        "measurement": "sensor_data",
        "tags": {
            "department": department.name,
            "sensor": sensor.name,
        },
        "fields": {
            "temperature": sensor.temperature,
            "oxygen_level": sensor.oxygen_level,
        },
    }

    client.write_points([sensor_data])
    print(f"Generated and stored sensor data: {sensor_data}")
    return f"Generated and stored sensor data: {sensor_data}"
