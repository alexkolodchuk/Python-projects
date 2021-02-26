from tkinter import *
from time import sleep
import _tkinter, sys

Vy = 0
dura = 1.5

tk = Tk()
tk.title("Program 1")
tk.wm_attributes("-topmost", 1)
cv = Canvas(tk, width = 750, height = 750)
cv.pack()
size = float(input("Write size: "))
color = input("Write color: ")

try:
    cv.create_oval(375-size/2, 50, 375+size/2, 50+size, fill=color)
except _tkinter.TclError:
    sys.exit()
coords = cv.coords(1)
cv.move(1, 0, Vy)

while True:
    cv.move(1, 0, Vy)
    Vy += 0.098
    coords = cv.coords(1)
    print("[SYSTEM] coords = "+str(coords))
    if coords[3] <= 750 and coords[3] >= 750-size/2:
        print("gravity flip")
        Vy = -Vy
        Vy /= dura
        
    sleep(0.01)
    try:
        tk.update()
        tk.update_idletasks()
    except _tkinter.TclError:
        sys.exit()
