from turtle import *


def draw_arrow():
    title("Arrow Directions") 
    bgcolor('light grey')
    shape("arrow")
    directions = [
        (0, "East", "left"),
        (90, "North", "center"),
        (180, "West", "right"),
        (270, "South", "center")
    ]
    for heading, name, alignment in directions:
        home()
        setheading(heading)
        forward(80)
        stamp() 
        forward(10) 
        write(name, align=alignment,) 

    hideturtle()
    exitonclick()

def draw_snake():
    import turtle as t
    t.setup(1000, 400, 200, 200)
    t.penup()
    t.fd(-150)
    t.pendown()
    t.seth(-40)
    t.pensize(25)
    t.pencolor("purple")
    for i in range(4):
        t.circle(40, 80)
        t.circle(-40, 80)
    t.circle(40, 80 / 2)
    t.fd(40)
    t.circle(16, 180)
    t.fd(40 * 2 / 3)
    t.done()

print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Please select what you want to draw:\n"
              " (1 for arrow, 2 for rainbow)\n"
              "Your selection is: ")
    try:
        a = eval(a)
        if a == 1:
            draw_arrow()
        elif a == 2:
            draw_snake()
        else:
            print("Please input the value in [1,2].")
    except:
        print("Please input the value in [1,2].")
