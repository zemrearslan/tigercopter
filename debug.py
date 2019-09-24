from time import time

from moves import Milliseconds


def assert_speed(speed: float):
    assert speed >= 10 and speed <= 100, f"Invalid speed of {speed}, must be >= 10 and <= 100"


async def timed_execution(f) -> Milliseconds:
    start = time()
    await f
    return (time() - start) * 1000.0
