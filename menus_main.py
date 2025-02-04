import time
import sys
from art import tprint

def typing_print(text, delay=0.05, split='word'):
    if split == 'letter':
        for i, char in enumerate(text):
            print(char, end='', flush=True)
            time.sleep(delay)
    elif split == 'word':
        words = text.split(' ')
        for word in words:
            if "\n" in word:  # observe newline
                print(word, end='', flush=True)
            else:
                print(word, end=' ', flush=True)
            time.sleep(delay)

def spinny_wheel(seconds=3):
    animation = "|/-\\"
    start_time = time.time()
    while True:
        # for i in range(4):
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        if time.time() - start_time > seconds:
            break
    sys.stdout.write("\r \n")

    
def welcome_menu():
    typing_print("Welcome to\n\n", split="letter")
    tprint("Whipped Pass Py", font="big")
    time.sleep(1)
    typing_print("Whipping up passwords as easy as. . . . 🥧\nLet's create a password system for you!\n", split="letter")
    spinny_wheel()
    typing_print("We'll start by getting a few words followed by a few numbers that are memorable to you but would be difficult for someone to guess.\n\n")
    input(("Press enter to continue.\n"))

