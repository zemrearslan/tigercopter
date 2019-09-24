import asyncio

from tello import tello
from moves import flip, FlipDirection, forward, back, left, right

class State:
    running = True
    moves = []


state = State()


def stop():
    state.running = False


def schedule(move):
    state.moves.insert(0, move)


async def scheduler():
    print("START")

    while state.running:
        if state.moves:
            next = state.moves.pop()
            await next()

        await asyncio.sleep(0.5)

    print("END")
    tello.end()


if __name__ == '__main__':
    asyncio.run(scheduler())
