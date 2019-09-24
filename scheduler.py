import asyncio
from audioop import max
from time import time

from macarena_moves import MACARENA
from tello import tello
from moves import flip, FlipDirection, forward, back, left, right, wait, takeoff, land, beats2ms


async def scheduler(moves):
    remaining_moves = list(moves)
    print("START")
    await takeoff()
    await asyncio.sleep(5)

    while remaining_moves:
        started = time()
        next_move, beats_budget = remaining_moves.pop()
        await next_move(beats_budget)
        ended = time()
        remaining_time_for_move = started + beats2ms(beats_budget)/1000 - ended

        if remaining_time_for_move < 0:
            print("WARNING: Move taken too long. Remaining time: ", remaining_time_for_move)
        else:
            await asyncio.sleep(remaining_time_for_move)

    print("END")

    await wait(500)
    await land()
    tello.end()


if __name__ == '__main__':
    asyncio.run(scheduler(MACARENA))
