import alarm
import board
import time
import microcontroller
import ssl
import socketpool
import wifi
import adafruit_minimqtt.adafruit_minimqtt as MQTT

# Add a secrets.py to your filesystem that has a dictionary called secrets with "ssid" and
# "password" keys with your WiFi credentials. DO NOT share that file or commit it into Git or other
# source control.
# pylint: disable=no-name-in-module,wrong-import-order
try:
    import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

# Set your Adafruit IO Username and Key in secrets.py
# (visit io.adafruit.com if you need to create an account,
# or if you need your Adafruit IO key.)
aio_username = secrets.ADAFRUIT_IO_USERNAME
aio_key = secrets.ADAFRUIT_IO_KEY

print("Connecting to %s" % secrets.ssid)
wifi.radio.connect(secrets.ssid, secrets.password)
print("Connected to %s!" % secrets.ssid)
### Feeds ###

# Setup a feed named 'photocell' for publishing to a feed
photocell_feed = aio_username + "/feeds/temperature"

### Code ###

# Define callback methods which are called when events occur
# pylint: disable=unused-argument, redefined-outer-name
def connected(client, userdata, flags, rc):
    # This function will be called when the client is connected
    # successfully to the broker.
    print("Connected to Adafruit IO!")
    # Subscribe to all changes on the onoff_feed.
    # client.subscribe(onoff_feed)


def disconnected(client, userdata, rc):
    # This method is called when the client is disconnected
    print("Disconnected from Adafruit IO!")


def message(client, topic, message):
    # This method is called when a topic the client is subscribed to
    # has a new message.
    print("New message on topic {0}: {1}".format(topic, message))


# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

# Set up a MiniMQTT Client
mqtt_client = MQTT.MQTT(
    broker="io.adafruit.com",
    # port=secrets["port"],
    username=aio_username,
    password=aio_key,
    socket_pool=pool,
    ssl_context=ssl.create_default_context(),
)

# Setup the callback methods above
mqtt_client.on_connect = connected
mqtt_client.on_disconnect = disconnected
mqtt_client.on_message = message

# Connect the client to the MQTT broker.
print("Connecting to Adafruit IO...")
mqtt_client.connect()

photocell_val = 0

# Poll the message queue
# mqtt_client.loop()

# Send a new message
temp = microcontroller.cpu.temperature
print("Sending temperature value: %d..." % microcontroller.cpu.temperature)
mqtt_client.publish(photocell_feed, microcontroller.cpu.temperature)

print("Sent!")


time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + 60)
alarm.exit_and_deep_sleep_until_alarms(time_alarm)