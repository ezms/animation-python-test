import sys, os, time
from sys import platform

MESSAGE = """
    |------------------------------------------------------------------------|
    |                                                                        |
    |                                                                        |
    |                       Kobra Termianl Typing Animation                  |
    |                                                                        |
    |                                                                        |
    |------------------------------------------------------------------------|
    |                                                                        |
    |                       Do you like pizza?                               |
    |                                                                        |
    |------------------------------------------------------------------------|
    |                                                                        |
    |                       Do you like cats?                                |
    |                                                                        |
    |------------------------------------------------------------------------|
    |                                                                        |
    |                       Do you like typing like me?                      |
    |                                                                        |
    |------------------------------------------------------------------------|
"""

def typing_animation(message):
    for character in message:
        sys.stdout.write(character)
        sys.stdout.flush()

        if character != "\n": time.sleep(.04)
        else: time.sleep(.7) 

if "linux" or "linux2" or "darwin" in platform: os.system("clear")
elif platform == "win32": os.system("cls")
else: print("Sorry, I don't know which system you are using (; -;)")

typing_animation(MESSAGE)