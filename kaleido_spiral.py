import turtle

def draw_circle(size):
    turtle.pencolor('Red')
    turtle.circle(size)
    draw_circle(size)

turtle               
from itertools import cycle
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])


def draw_circle(size,angle,shift):
    turtle.bgcolor(next(colors))
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+0.5, angle+1,shift+1)
    
turtle.bgcolor('black')
turtle.speed('fastest')
turtle.pensize(5)
draw_circle(30,0,1)
