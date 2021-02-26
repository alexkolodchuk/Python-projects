import turtle
from multiprocessing import Process
from threading import Thread
import time
import _tkinter
import sys

g = turtle.Turtle()
scr = turtle.Screen()
scr.setup(width=800, height=600)
#g.up()
ground = turtle.Turtle()
ground.up()
ground.goto(-400, -200)
ground.down()
ground.goto(400, -200)
ground.up()

'''class Keys(Thread):

    def __init__(self, screen, t):
        Thread.__init__(self)
        self.screen = screen
        self.t = t

    def fw():
        self.t.forward(5)

    def bw():
        self.t.backward(5)

    def r():
        self.t.right(5)

    def l():
        self.t.left(5)

    def run(self):
        self.screen.onkeypress(fw, "Up")
        self.screen.onkeypress(bw, "Down")
        self.screen.onkeypress(r, "Right")
        self.screen.onkeypress(l, "Left")

        self.screen.listen()
        self.screen.mainloop()

class Gravity(Thread):

    def __init__(self, t):
        Thread.__init__(self)
        self.t = t
        self.x = t.pos()[0]
        self.y = t.pos()[1]

    def run(self):
        while True:
            self.t.goto(self.x, self.y-9.8)
            time.sleep(1)

def main(screen, turtle):
    k = Keys(screen, turtle)
    gr = Gravity(turtle)
    k.start()
    gr.start()

if __name__ == "__main__":
    main(scr, g)
'''
#
'''def fw():
    g.forward(15)

def bw():
    g.backward(15)

def r():
    g.right(15)

def l():
    g.left(15)

while True:
    scr.onkeypress(fw, "Up")
    scr.onkeypress(bw, "Down")
    scr.onkeypress(r, "Right")
    scr.onkeypress(l, "Left")

    scr.listen()

    g.goto(g.pos()[0], g.pos()[1]-9.8)
    print("gr")
    time.sleep(0.1)'''
#
def v(x, y):
    g.goto(g.pos()[0]+x, g.pos()[1]+y)
'''t = 0
chy = 20
while True:
    x = g.pos()[0]
    y = g.pos()[1]
    print(x, y)
    chx = 0
    if int(x)==-400 or int(x)==400:
        chx = 0
    if int(y)<=-200 or int(y)==300:
        t = 0
        g.goto(g.pos()[0], -190)
    chy -= 9.8*t
    try:
        v(chx, chy)
    except _tkinter.TclError:
        sys.exit()
    t += 0.01
    time.sleep(0.01)'''

t = 0
g.speed(100)
g.goto(0, 280)
n = 2
while True:
    v(2, n-0.98*t)
    if g.pos()[1] <= -200:
        g.goto(g.pos()[0], -199)
        t = 0
        n /= 2
    t += 0.1
    time.sleep(0.1)
