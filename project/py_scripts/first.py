import network 
import socket 
import time 
from machine import Pin, PWM 

# ----------- Wi-Fi Setup ------------ 
ssid = 'Telstra84780E' 
password = 'ppaheu55xw' 

wlan = network.WLAN(network.STA_IF) 
wlan.active(True) 
wlan.connect(ssid, password) 

print("Connecting to WiFi...", end="") 
while not wlan.isconnected(): 
    print(".", end="") 
    time.sleep(1) 

print("\nConnected!") 
ip = wlan.ifconfig()[0] 
print("Pico Web Server IP:", ip) 

# ----------- Servo Setup ------------ 
servo_left = PWM(Pin(0))   # Left wheel 
servo_right = PWM(Pin(1))  # Right wheel 
servo_left.freq(50) 
servo_right.freq(50) 

# Helper: Convert speed to servo PWM 
def set_speed(servo, speed): 
    base = 1.5  # ms (stop) 
    pulse = base + (speed * 0.5)  # -1 to 1 
    duty = int(pulse / 20 * 65535) 
    servo.duty_u16(duty) 

# Movement helpers based on your setup 
def move_forward(duration): 
    set_speed(servo_left, -1)   # Left spins backward 
    set_speed(servo_right, 1)   # Right spins forward 
    time.sleep(duration) 
    stop() 

def move_backward(duration): 
    set_speed(servo_left, 1) 
    set_speed(servo_right, -1) 
    time.sleep(duration) 
    stop() 

def turn_left(duration): 
    set_speed(servo_left, -1) 
    set_speed(servo_right, -1) 
    time.sleep(duration) 
    stop() 

def turn_right(duration): 
    set_speed(servo_left, 1) 
    set_speed(servo_right, 1) 
    time.sleep(duration) 
    stop() 

def stop(): 
    set_speed(servo_left, 0) 
    set_speed(servo_right, 0) 

# Warehouse tasks 
def go_to_aisle_1(): 
    print("Going to Aisle 1") 
    move_forward(2)      # move to aisle 
    turn_right(0.9)      # turn into aisle 
    move_forward(1.5)    # move down aisle 
    stop() 
    time.sleep(1) 
    move_backward(1.5)   # return 
    turn_left(0.9)       # turn to original heading 
    move_backward(2) 
    stop() 

def go_to_aisle_2(): 
    print("Going to Aisle 2") 
    move_forward(3) 
    turn_right(0.9) 
    move_forward(1.5) 
    stop() 
    time.sleep(1) 
    move_backward(1.5) 
    turn_left(0.9) 
    move_backward(3) 
    stop() 

html = """<!DOCTYPE html>
<html>
<head>
  <title>Warehouse Robot</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Kanit', sans-serif;
    }
    body {
      background-image: url('https://i.postimg.cc/SKbnzyb4/Copilot-20250624-195441.png'); 
      background-size: cover;
      background-position: center;
      background-repeat: no-repeat;
      height: 100vh;
      color: #eee;
      text-align: center;
    }
    .navbar {
      background: rgba(220, 20, 60, 0.7);
      height: 80px;
      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 1.2rem;
      position: sticky;
      top: 0;
      z-index: 999;
      gap: 12px; /* space between logo and text */
    }
    .navbar-logo {
      height: 40px;
      width: 40px;
      fill: #fff;
      flex-shrink: 0;
    }
    #navbar__logo {
      font-size: 1.8rem;
      background-image: linear-gradient(to top, #420f7c 50%, #975bc9 100%);
      background-clip: text;
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      cursor: default;
    }
    button {
      font-size: 20px;
      margin: 10px;
      padding: 15px 30px;
      border: none;
      border-radius: 8px;
      cursor: pointer;
    }
    .task {
      background: #3498db;
      color: white;
      transition: background 0.3s ease;
    }
    .task:hover {
      background: #2980b9;
    }
  </style>
</head>
<body>
  <nav class="navbar">
    <!-- Warehouse box SVG icon -->
    <svg xmlns="http://www.w3.org/2000/svg" class="navbar-logo" viewBox="0 0 16 16" fill="currentColor" aria-hidden="true">
      <path d="M8.277 1.199a.5.5 0 0 0-.554 0L1.64 5.363a.5.5 0 0 0-.275.439v5.91a.5.5 0 0 0 .738.441l5.095-2.98a.5.5 0 0 1 .508 0l5.095 2.98a.5.5 0 0 0 .738-.44v-5.91a.5.5 0 0 0-.276-.44L8.277 1.2zM2.036 6.116 8 3.193l5.965 2.923-1.482.87L8 5.638 3.519 6.98l-1.483-.864zm-1.06 6.96v-5.207l2.252 1.318v4.875L.976 13.076zm5.947 1.07-4.61-2.7v-4.875l4.61 2.698 4.61-2.698v4.875l-4.61 2.7zm5.197-1.07-2.252-1.318v-4.875l2.252-1.318v5.207z"/>
    </svg>
    <div id="navbar__logo">Warehouse Robot</div>
  </nav>

  <form method="GET">
    <h2>Select a Task:</h2>
    <button class="task" name="task" value="aisle1">Go to Aisle 1</button>
    <button class="task" name="task" value="aisle2">Go to Aisle 2</button>
    <button class="task" name="task" value="stop">STOP</button>
  </form>
</body>
</html>
"""

# ----------- Web Server ------------ 
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1] 
server = socket.socket() 
server.bind(addr) 
server.listen(1) 
print("Server running on http://%s" % ip) 

while True: 
    client, addr = server.accept() 
    print("Client connected from", addr) 
    request = client.recv(1024) 
    request = str(request) 

    if 'task=aisle1' in request: 
        go_to_aisle_1() 
    elif 'task=aisle2' in request: 
        go_to_aisle_2() 
    elif 'task=stop' in request: 
        stop() 

    client.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n') 
    client.send(html) 
    client.close() 
