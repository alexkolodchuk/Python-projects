from turtle import *

def makegrid():
    
    w5m = Turtle()
    w4m = Turtle()
    w3m = Turtle()
    w2m = Turtle()
    w1m = Turtle()
    w0 = Turtle()
    w1 = Turtle()
    w2 = Turtle()
    w3 = Turtle()
    w4 = Turtle()
    w5 = Turtle()
    s5m = Turtle()
    s4m = Turtle()
    s3m = Turtle()
    s2m = Turtle()
    s1m = Turtle()
    s0 = Turtle()
    s1 = Turtle()
    s2 = Turtle()
    s3 = Turtle()
    s4 = Turtle()
    s5 = Turtle()
    
    grid = [w5m, w4m, w3m, w2m, w1m, w0, w1, w2, w3, w4, w5, s5m, s4m, s3m, s2m, s1m, s0, s1, s2, s3, s4, s5]
    grdw = [w5m, w4m, w3m, w2m, w1m, w0, w1, w2, w3, w4, w5]
    grds = [s5m, s4m, s3m, s2m, s1m, s0, s1, s2, s3, s4, s5]
    
    for t in range(0, len(grid)):
        print("[SYSTEM] Current identificator to "+str(grid[t])+" is "+str(t))
        grid[t].up()
        #grid[t].color("grey")

    w5m.goto(-250, 250)
    w4m.goto(-200, 250)
    w3m.goto(-150, 250)
    w2m.goto(-100, 250)
    w1m.goto(-50, 250)
    w0.goto(0, 250)
    w1.goto(50, 250)
    w2.goto(100, 250)
    w3.goto(150, 250)
    w4.goto(200, 250)
    w5.goto(250, 250)

    for t in range(0, len(grdw)):
        grdw[t].right(90)
        grdw[t].down()
        grdw[t].forward(500)
        grdw[t].hideturtle()

    s5m.goto(-250, 250)
    s4m.goto(-250, 200)
    s3m.goto(-250, 150)
    s2m.goto(-250, 100)
    s1m.goto(-250, 50)
    s0.goto(-250, 0)
    s1.goto(-250, -50)
    s2.goto(-250, -100)
    s3.goto(-250, -150)
    s4.goto(-250, -200)
    s5.goto(-250, -250)

    for t in range(0, len(grds)):
        grds[t].down()
        grds[t].forward(500)
        grds[t].hideturtle()
        
makegrid()
