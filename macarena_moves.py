from debug import assert_speed, timed_execution
from moves import Distance, beats2ms, up, right, down, left, flip, FlipDirection, set_speed


async def vertical_square(beats: int, dist: Distance = 20):
    buffer_ms = 1000
    time_ms = beats2ms(beats) - buffer_ms
    time_per_move_ms = time_ms / 4
    required_speed = int((dist / (time_per_move_ms / 1000.0)))
    assert_speed(required_speed)

    elapsed_ms = await timed_execution(set_speed(required_speed))
    print(f'set time in {elapsed_ms}ms')

    await up(dist)
    await right(dist)
    await down(dist)
    await left(dist)


async def turn_upside_down(beats: int):
    await flip(FlipDirection.FORWARD)


async def vertical_zig_zag(beats: int):
    pass


MACARENA = [(vertical_square, 8)]
