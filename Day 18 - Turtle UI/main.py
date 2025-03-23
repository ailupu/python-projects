from turtle import Turtle, Screen
import random

timi_the_turtle = Turtle()
timi_the_turtle.shape('turtle')
timi_the_turtle.color('OliveDrab')

# Draw A Square wiht Timi The Turtle
for _ in range(4):
    timi_the_turtle.forward(100)
    timi_the_turtle.left(90)

#Draw a dashed line
for _ in range(20):
    timi_the_turtle.forward(10)
    timi_the_turtle.penup()
    timi_the_turtle.forward(10)
    timi_the_turtle.pendown()

#Draw a triangle, square, pentagon, hexagon, helptagon, octagon, nonagon, decagon
colors = ["red", "green", "pink", "blue", "coral", "cyan", "black", "aquamarine"]
num_sides = [3,4,5,6,7,8,9,10]
for i in num_sides:
    for _ in range(i):
        color_random = random.choice(colors)
        timi_the_turtle.color(color_random)
        angle = 360 / i
        timi_the_turtle.forward(100)
        timi_the_turtle.right(angle=angle)

#Draw a random walk
timi_the_turtle.speed('fastest')
for _ in range(500):
    timi_the_turtle.color(random.choice(colors))
    timi_the_turtle.pensize(10)
    directions = [0, 90, 180, 270]
    timi_the_turtle.forward(30)
    timi_the_turtle.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()