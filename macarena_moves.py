from debug import assert_speed, timed_execution
from moves import Distance, beats2ms, up, right, down, left, flip, FlipDirection, set_speed, wait, required_speed


async def vertical_square(beats: int, dist: Distance = 20):
    buffer_ms = 400
    time_ms = beats2ms(beats) - buffer_ms
    time_per_move_ms = time_ms / 4
    speed = required_speed(time_per_move_ms, dist)
    print(f"TIME AVAILABLE = {time_ms/1000}s")
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


async def turn_upside_down(beats: int):
    await flip(FlipDirection.FORWARD)


async def vertical_zig_zag(beats: int):
    pass

MACARENA = [(vertical_square, 8)]
