import json
import time

import paho.mqtt.client as mqtt

id = ''  # your device id

client_telemetry_topic = f'{id}/telemetry'
server_command_topic = f'{id}/commands'
client_name = f'{id}-cloud-server'

mqtt_client = mqtt.Client(client_name)
mqtt_client.connect('test.mosquitto.org')

mqtt_client.loop_start()

def handle_telemetry(client, data, msg):
    payload = json.loads(msg.paylod.decode())
    print("Message received: ", payload)

    command = { 'led_on' : payload['light'] < 300 }
    print("Sending message: ", command)

    client.publish(server_command_topic, json.dumps(command))

mqtt_client.subscribe(client_telemetry_topic)
mqtt_client.on_message = handle_telemetry

while True:
    time.sleep(1)