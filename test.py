from djitellopy import Tello
import time

tello = Tello()

tello.connect()
tello.takeoff()
tello.move_left(100)
tello.rotate_counter_clockwise(45);
tello.land()
tello.end()