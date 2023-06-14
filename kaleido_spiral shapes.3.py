import turtle

from itertools import cycle
colors = cycle(['red','orange','yellow','green','blue','purple'])

def draw_shape(size,angle,shift,shape):
    turtle.pencolor(next(colors))
    next_shape=''
    if shape == 'circle':
        turtle.circle(size)
        next_shape= 'square'
    elif shape =='square':
        for i in range(3):
            turtle.forward(size+80)
            turtle.left(120)
        next_shape = 'circle'
    turtle.right(angle)
    turtle.forward(shift)
    draw_shape(size + 0,angle+0,shift+0,next_shape)



turtle.bgcolor('black')
turtle.speed('fastest')
turtle.pensize(4)
draw_shape(30,3,1, 'circle')
