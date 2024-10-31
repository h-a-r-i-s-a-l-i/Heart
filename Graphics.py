import turtle
t = turtle.Turtle()
def curve():
    t.left(90)
    for i in range (12):
        t.forward(20)
        t.left(15)
def heart():
    t.pu()
    t.goto(-50,-15)
    t.pd()
    t.begin_fill()
    t.goto(100,175)
    curve()
    t.left(105)
    curve()
    t.goto(-50,-15)
def write(txt):
    t.pu()
    t.setpos(-130,125)
    t.pd()
    t.color("lightgreen")
    t.write(txt,font=("Verdana", 30, "bold"))
    t.hideturtle()
def main():
    t.pensize(4)
    t.color("black","red")
    t.begin_fill() 
    heart()
    t.end_fill()
    write("Weirdo")
main()
turtle.done()
