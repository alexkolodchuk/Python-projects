import keyboard
from winsound import *
import sys
def l1():
    PlaySound(Beep(1000, 400), SND_ASYNC)
def h1():
    PlaySound(Beep(1000, 150), SND_ASYNC)

def l2():
    PlaySound(Beep(2000, 400), SND_ASYNC)
def h2():
    PlaySound(Beep(2000, 150), SND_ASYNC)

def l3():
    PlaySound(Beep(3000, 400), SND_ASYNC)
def h3():
    PlaySound(Beep(3000, 150), SND_ASYNC)

def l4():
    PlaySound(Beep(4000, 400), SND_ASYNC)
def h4():
    PlaySound(Beep(4000, 150), SND_ASYNC)

def l5():
    PlaySound(Beep(5000, 400), SND_ASYNC)
def h5():
    PlaySound(Beep(5000, 150), SND_ASYNC)

def l6():
    PlaySound(Beep(6000, 400), SND_ASYNC)
def h6():
    PlaySound(Beep(6000, 150), SND_ASYNC)

def l7():
    PlaySound(Beep(7000, 400), SND_ASYNC)
def h7():
    PlaySound(Beep(7000, 150), SND_ASYNC)

def l8():
    PlaySound(Beep(8000, 400), SND_ASYNC)
def h8():
    PlaySound(Beep(8000, 150), SND_ASYNC)

def l9():
    PlaySound(Beep(9000, 400), SND_ASYNC)
def h9():
    PlaySound(Beep(9000, 150), SND_ASYNC)

def ex():
    sys.exit()
    exit()

keyboard.add_hotkey('q', l1)
keyboard.add_hotkey('w', l2)
keyboard.add_hotkey('e', l3)
keyboard.add_hotkey('r', l4)
keyboard.add_hotkey('t', l5)
keyboard.add_hotkey('y', l6)
keyboard.add_hotkey('u', l7)
keyboard.add_hotkey('i', l8)
keyboard.add_hotkey('o', l9)

keyboard.add_hotkey('a', h1)
keyboard.add_hotkey('s', h2)
keyboard.add_hotkey('d', h3)
keyboard.add_hotkey('f', h4)
keyboard.add_hotkey('g', h5)
keyboard.add_hotkey('h', h6)
keyboard.add_hotkey('j', h7)
keyboard.add_hotkey('k', h8)
keyboard.add_hotkey('l', h9)

keyboard.add_hotkey('Enter', ex)
