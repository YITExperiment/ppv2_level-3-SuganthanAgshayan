import turtle

def draw_circle(size):
    turtle.pencolor('Red')
    turtle.circle(size)
    draw_circle(size)

turtle               
from itertools import cycle
colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])


def draw_circle(size,angle,shift):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size+0, angle+0,shift+0)
    
turtle.bgcolor('hotpink')
turtle.speed('fastest')
turtle.pensize(5)
draw_circle(90,3,0)
