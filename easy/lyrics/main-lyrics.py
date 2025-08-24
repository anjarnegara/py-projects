import sys
from rich import print
from time import sleep
import time


def printLyrics():
    lines = [
        ("............", 1.00),
        ("La-la-la-la", 0.06),
        ("Ri-ri-ras, ri-ras-ra-ra-ti-ti-ti-ta", 0.05),
        ("Ra-ri-ras, ra-ra--ti-ti-ti-tas-ti-ti", 0.07),
        ("Rastis! Rastis! Ra-ti-ti-la!", 0.03),
        ("..................", 0.30),
        ("Let's start a new life from the darkness", 33.00),
        ("Until the light reveals the end", 36.00),
        ("Fear, hatred, sorrow, desperation ", 40.00),
        ("Even you look miserable ", 43.00),
        ("Look down from above, I feel awful ", 46.00),
        ("The time has come, lets all go home ", 50.00),
        ("Sinister faces, growing curses", 54.00),
        ("This is my last war.. la-la-la", 56.00),
    ]

    for line, delay in lines:
        print(line)
        sleep(delay)

printLyrics()