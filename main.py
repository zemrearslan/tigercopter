import asyncio

from moves import right, left, back, forward
from tello import tello
from scheduler import scheduler, schedule, stop


async def dance_move():
    await forward(30)
    await back(30)
    await left(30)
    await right(30)
    stop()

schedule(dance_move)

asyncio.run(scheduler())
