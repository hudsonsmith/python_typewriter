from sys import stdout
from time import sleep

def typewrite(string: str, sleep_time: int=0.04) -> None:
    """A function to typewrite something to the screen."""

    for char in string:
        stdout.write(char)
        stdout.flush()
        sleep(sleep_time)
