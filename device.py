import sys
import json
import random
import time
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient


class Device:

    # ------------------------------------------------------------------------------------------------

    def __init__(self):
        pass

    # ------------------------------------------------------------------------------------------------

    @classmethod
    def connect(cls, endpoint, client_id):
        mqtt_client = AWSIoTMQTTClient(client_id, useWebsocket=False)

        mqtt_client.configureCredentials(
            "aws-iot-root-ca.pem", "{}-private.pem.key".format(client_id), "{}-certificate.pem.crt".format(client_id))

        mqtt_client.configureEndpoint(endpoint, 8883)
        mqtt_client.configureAutoReconnectBackoffTime(1, 32, 20)
        mqtt_client.configureOfflinePublishQueueing(-1)
        mqtt_client.configureDrainingFrequency(2)
        mqtt_client.configureConnectDisconnectTimeout(10)
        mqtt_client.configureMQTTOperationTimeout(5)
        print("try to connect {} ...".format(endpoint))
        mqtt_client.connect()
        print("connected")
        cls.client_id = client_id
        cls.mqtt_client = mqtt_client

    # ------------------------------------------------------------------------------------------------

    @classmethod
    def publish(cls, value):
        payload = {
            "value": value
        }
        print("try to publish message for {} ...".format(cls.client_id))
        cls.mqtt_client.publish("device/{}".format(cls.client_id), json.dumps(payload), 1)
        print("published")

    # ------------------------------------------------------------------------------------------------

    @classmethod
    def subscribe(cls):
        def _message_from_iot_gw(client, userdata, message):
            print(json.loads(message.payload))

        print("try to subscribe for messages to {} ...".format(cls.client_id))
        cls.mqtt_client.subscribe("device/{}".format(cls.client_id), 1, _message_from_iot_gw)
        print("subscribed")

    # ------------------------------------------------------------------------------------------------


if __name__ == "__main__":

    Device.connect(sys.argv[1], sys.argv[2])

    Device.subscribe()

    while True:

        value = 50 + int(random.random() * 50)
        Device.publish(value)

        time.sleep(5)
