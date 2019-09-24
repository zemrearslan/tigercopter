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


async def flip(direction: FlipDirection):
    tello.flip(direction.value)
    await wait(400)


async def wait(ms: Milliseconds):
    await asyncio.sleep(ms / 1000.0)


async def up(dist: Distance):
    assert dist >= 20 and dist <= 500
    tello.move_up(dist)
    await wait(guess_move_time(dist))


async def down(dist: Distance):
    assert dist >= 20 and dist <= 500
    tello.move_down(dist)
    await wait(guess_move_time(dist))


async def left(dist: Distance):
    assert dist >= 20 and dist <= 500
    tello.move_left(dist)
    await wait(guess_move_time(dist))


async def right(dist: Distance):
    assert dist >= 20 and dist <= 500
    tello.move_right(dist)
    await wait(guess_move_time(dist))


async def forward(dist: Distance):
    assert dist >= 20 and dist <= 500
    tello.move_forward(dist)
    await wait(guess_move_time(dist))


async def back(dist: Distance):
    assert dist >= 20 and dist <= 500
    tello.move_back(dist)
    await wait(guess_move_time(dist))

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

def guess_move_time(dist: Distance) -> Milliseconds:
    return 50 + int(dist * 50)

