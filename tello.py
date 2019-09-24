from unittest.mock import Mock

from djitellopy import Tello
import sys

mock = len(sys.argv) > 1 and sys.argv[1] == 'dryrun'

if mock:
    print("(MOCKING TELLO)")
    tello = Mock(Tello)
else:
    tello = Tello()
    tello.RESPONSE_TIMEOUT = 10
    tello.TIME_BTW_COMMANDS = 1
    tello.connect()
