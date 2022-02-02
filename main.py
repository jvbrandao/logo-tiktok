
import turtle

lapis = turtle.Turtle()
lapis.width(20)
turtle.Screen().bgcolor("grey")
colors = ['#db0f3c', '#50ebe7', 'white']
pos = [(0, 0), (-5, 13), (-5, 5)]

for (x, y), col in zip(pos, colors):
    lapis.up()
    lapis.goto(x,y)
    lapis.down()
    lapis.color(col)
    lapis.left(180)
    lapis.circle(50, 270)
    lapis.forward(120)
    lapis.left(180)
    lapis.circle(50, 90)