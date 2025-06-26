import sys
import time
import network
from machine import Pin
from robot import Robot
from web_server import WebServer

# WiFi Setup
SSID = 'Telstra84780E'
PASSWORD = 'ppaheu55xw'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

print("Connecting to WiFi...", end="")
while not wlan.isconnected():
    print(".", end="")
    time.sleep(1)

print("\nConnected!")
ip = wlan.ifconfig()[0]
print(f"Pico Web Server IP: {ip}")

# Stop Pin Setup
stop_pin = Pin(4, Pin.IN, Pin.PULL_UP)

def callback(_):
    raise KeyboardInterrupt("Stop pin pressed")

stop_pin.irq(trigger=Pin.IRQ_FALLING, handler=callback)

# Instantiate Robot and Server
robot = Robot()
server = WebServer(robot, ip)

# Main Loop
try:
    server.start()
except KeyboardInterrupt as e:
    print("\nKeyboardInterrupt:", e)
    sys.print_exception(e)
