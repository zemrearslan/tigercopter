import asyncio

from macarena_moves import MACARENA
from moves import right, left, back, forward, wait
from tello import tello
from scheduler import scheduler


async def dance_move():
    await forward(30)
    await back(30)
    await left(30)
    await right(30)
    await wait(500)


asyncio.run(scheduler(MACARENA))
