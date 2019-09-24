import asyncio
from enum import Enum
from tello import tello

from djitellopy import Tello

Distance = int
Milliseconds = float
Speed = int
""" 10 - 100 """

BPM = 103


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

async def curve(x1:Distance, y1:Distance, z1:Distance, x2:Distance, y2:Distance, z2:Distance, speed:int):
    assert x1 >= 20 and x1 <= 500
    assert x2 >= 20 and x2 <= 500
    assert y1 >= 20 and y1 <= 500
    assert y2 >= 20 and y2 <= 500
    assert z1 >= 20 and z1 <= 500
    assert z2 >= 20 and z2 <= 500
    assert speed >= 10 and speed <=60
    tello.go_xyz_speed(x1, y1, z1, x2, y2, z2, speed)
    await wait(10)

async def rotate(degrees: float):
    # expects a number between 1 and 3600
    if degrees >= 0:
        tello.rotate_clockwise(degrees * 10)
    else:
        tello.rotate_counter_clockwise(-degrees * 10)


async def set_speed(speed: int):
    assert speed >= 10 and speed <= 100, f'invalid speed - {speed}'
    tello.set_speed(speed)


def required_speed(time_ms: float, distance: Distance) -> int:
    return int((distance / (time_ms / 1000.0)))


def beats2ms(beats: int) -> Milliseconds:
    return (beats / BPM) * 60 * 1000
