import asyncio
from enum import Enum
from tello import tello

from djitellopy import Tello

Distance = int
Milliseconds = int


class FlipDirection(Enum):
    LEFT = 'l'
    RIGHT = 'r'
    FORWARD = 'f'
    BACKWARD = 'b'


async def takeoff():
    tello.takeoff()


async def land():
    tello.land()


async def flip(direction: FlipDirection):
    tello.flip(direction.value)


async def wait(ms: Milliseconds):
    await asyncio.sleep(ms / 1000.0)


async def up(dist: Distance):
    assert dist >= 20 and dist <= 500
    tello.move_up(dist)


async def down(dist: Distance):
    assert dist >= 20 and dist <= 500
    tello.move_down(dist)


async def left(dist: Distance):
    assert dist >= 20 and dist <= 500
    tello.move_left(dist)


async def right(dist: Distance):
    assert dist >= 20 and dist <= 500
    tello.move_right(dist)


async def forward(dist: Distance):
    assert dist >= 20 and dist <= 500
    tello.move_forward(dist)


async def back(dist: Distance):
    assert dist >= 20 and dist <= 500
    tello.move_back(dist)


async def rotate(degrees: float):
    # expects a number between 1 and 3600
    if degrees >= 0:
        tello.rotate_clockwise(degrees * 10)
    else:
        tello.rotate_counter_clockwise(-degrees * 10)


async def set_speed(speed: float):
    assert speed >= 10 and speed <= 100, f'invalid speed - {speed}'
    tello.set_speed(speed)
