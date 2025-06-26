from machine import Pin, PWM, time_pulse_us
import time

class Robot:
    def __init__(self, trig_pin=2, echo_pin=3):
        # Servo Setup
        self.servo_left = PWM(Pin(0))
        self.servo_right = PWM(Pin(1))
        self.servo_left.freq(50)
        self.servo_right.freq(50)
        self.last_speed = 0.0

        # Ultrasonic Sensor Setup
        self.trig = Pin(trig_pin, Pin.OUT)
        self.echo = Pin(echo_pin, Pin.IN)

    def set_speed(self, servo, speed): 
        """Set servo speed from -1 (full backward) to 1 (full forward)."""
        base = 1.5
        pulse = base + (speed * 0.5)
        duty = int(pulse / 20 * 65535)
        servo.duty_u16(duty)
        self.last_speed = speed

    def stop(self): 
        self.set_speed(self.servo_left, 0) 
        self.set_speed(self.servo_right, 0)

    def get_distance(self): 
        self.trig.value(0)
        time.sleep_us(2)
        self.trig.value(1)
        time.sleep_us(10)
        self.trig.value(0)

        duration = time_pulse_us(self.echo, 1, 30000)
        distance = (duration / 2) / 29.1
        return distance

    def safe_move(self, move_func, duration, min_distance=15): 
        if self.get_distance() < min_distance:
            print(f"Obstacle detected within {min_distance}cm! Movement stopped.")
            self.stop()
            return
        move_func(duration)

    def move_forward(self, duration): 
        self.safe_move(lambda d: self._move_forward(d), duration)

    def move_backward(self, duration): 
        self._move_backward(duration)

    def turn_left(self, duration): 
        self.safe_move(lambda d: self._turn_left(d), duration)

    def turn_right(self, duration): 
        self.safe_move(lambda d: self._turn_right(d), duration)

    def _move_forward(self, duration): 
        self.set_speed(self.servo_left, -1) 
        self.set_speed(self.servo_right, 1) 
        time.sleep(duration) 
        self.stop()

    def _move_backward(self, duration): 
        self.set_speed(self.servo_left, 1) 
        self.set_speed(self.servo_right, -1) 
        time.sleep(duration) 
        self.stop()

    def _turn_left(self, duration): 
        self.set_speed(self.servo_left, -1) 
        self.set_speed(self.servo_right, -1) 
        time.sleep(duration) 
        self.stop()

    def _turn_right(self, duration): 
        self.set_speed(self.servo_left, 1) 
        self.set_speed(self.servo_right, 1) 
        time.sleep(duration) 
        self.stop()

    # Warehouse Tasks
    def go_to_aisle_1(self): 
        print("Going to Aisle 1") 
        self.move_forward(2) 
        self.turn_right(0.9) 
        self.move_forward(1.5) 
        time.sleep(1) 
        self.move_backward(1.5) 
        self.turn_left(0.9) 
        self.move_backward(2)

    def go_to_aisle_2(self): 
        print("Going to Aisle 2") 
        self.move_forward(3) 
        self.turn_right(0.9) 
        self.move_forward(1.5) 
        time.sleep(1) 
        self.move_backward(1.5) 
        self.turn_left(0.9) 
        self.move_backward(3)

    def go_to_aisle_3(self): 
        print("Going to Aisle 3")
        self.move_forward(4)
        self.turn_right(0.9)
        self.move_forward(1.5)
        time.sleep(1)
        self.move_backward(1.5)
        self.turn_left(0.9)
        self.move_backward(4)

    def go_to_aisle_4(self): 
        print("Going to Aisle 4")
        self.move_forward(5)
        self.turn_right(0.9)
        self.move_forward(1.5)
        time.sleep(1)
        self.move_backward(1.5)
        self.turn_left(0.9)
        self.move_backward(5)

    def go_to_aisle_5(self): 
        print("Going to Aisle 5")
        self.move_forward(6)
        self.turn_right(0.9)
        self.move_forward(1.5)
        time.sleep(1)
        self.move_backward(1.5)
        self.turn_left(0.9)
        self.move_backward(6)

    def go_to_aisle_6(self): 
        print("Going to Aisle 6")
        self.move_forward(7)
        self.turn_right(0.9)
        self.move_forward(1.5)
        time.sleep(1)
        self.move_backward(1.5)
        self.turn_left(0.9)
        self.move_backward(7)
