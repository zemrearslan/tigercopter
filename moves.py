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
    await wait(400)


async def land():
    tello.land()
    await wait(400)


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


def guess_move_time(dist: Distance) -> Milliseconds:
    return 50 + int(dist * 50)
