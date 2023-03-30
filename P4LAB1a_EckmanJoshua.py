# create turtle
import turtle
dave = turtle.Turtle()

# draw square
num = 0
while num < 4:
    dave.forward(75)
    dave.left(90)
    num = num + 1

# draw triangle
num = 0
while num < 3:
    dave.forward(75)
    dave.left(120)
    num = num + 1
