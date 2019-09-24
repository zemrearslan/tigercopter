from tello import tello
from debug import assert_speed, timed_execution
from moves import Distance, beats2ms, up, right, down, left, flip, FlipDirection, set_speed, wait, required_speed, \
    seconds2beats, curve, rotate, go


async def goes_up(beats: int):
    await up(100)


async def vertical_square(beats: int, dist: Distance = 100):
    buffer_ms = 400
    time_ms = beats2ms(beats) - buffer_ms
    time_per_move_ms = time_ms / 4
    speed = required_speed(time_per_move_ms, dist)
    print(f"TIME AVAILABLE = {time_ms / 1000}s")
    print(f"required speed = {speed}")
    assert_speed(speed)
    print(f'executing move in {time_ms}ms')

    elapsed_ms = await timed_execution(set_speed(speed))
    print(f'set speed in {elapsed_ms}ms')

    await up(dist)
    await wait(100)

    await right(dist)
    await wait(100)

    await down(dist)
    await wait(100)

    await left(dist)
    await rotate(90)


async def turn_upside_down(beats: int):
    await flip(FlipDirection.FORWARD)
    await rotate(90)


async def infinity(beats: int):
    await set_speed(50)
    # await flip(FlipDirection.RIGHT)
    tello.flip('r')
    await left(100)
    # await flip(FlipDirection.LEFT)
    tello.flip('l')
    await right(100)
    await rotate(90)


def arrange(f, seconds: int, loops: int):
    async def moves(beats: int):
        for i in range(loops):
            await f(int(beats / loops))

    beats = seconds2beats(seconds)
    return moves


async def vertical_zig_zag(beats: int):
    await go(0, 50, 50, 100)
    await rotate(180)
    await down(50)
    await rotate(90)
    await go(0, 50, 50, 100)
    await rotate(90)
    await down(50)
    await rotate(180)


async def turn_right():
    await rotate(90)


MACARENA = [
    (infinity, 8),
    (turn_upside_down, 8),
    (vertical_square, 8),
    (vertical_zig_zag, 8),
    # (arrange(vertical_square, 8, 2), 16),
] * 4
