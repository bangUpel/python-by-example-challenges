import turtle
import random

#first challenge
for i in range (0,4):
    turtle.forward(100)
    turtle.right(90)

#second challenge
for i in range(0,3):
    turtle.forward(100)
    turtle.left(120)

#third challenge
turtle.circle(100)

#fourth challenge
for i in range(0,3):
    for i in range(0,4):
        turtle.pendown()
        turtle.forward(100)
        turtle.left(90)
    turtle.penup()
    turtle.forward(150)
turtle.pendown()

#fifth challenge
for i in range (0,5):
    turtle.right(144)
    turtle.forward(100)

#sixth challenge
#one
turtle.left(90)
turtle.forward(100)

#two
turtle.right(90)
turtle.penup()
turtle.forward(20)
turtle.pendown()
for i in range (0,2):
    turtle.forward(50)
    turtle.right(90)
for i in range(0,3):
    turtle.forward(50)
    turtle.left(90)
turtle.penup()
turtle.right(90)
turtle.forward(20)

#three
turtle.pendown()
turtle.forward(80)
for i in range (0,2):
    for i in range (0,2):
        turtle.left(90)
        turtle.forward(50)
    turtle.left(90)
turtle.forward(80)

#seventh challenge
for i in range(0,8):
    color = random.choice(['yellow', 'red', 'blue', 'black', 'purple'])
    turtle.color(color)
    turtle.forward(100)
    turtle.right(45)

#eight challenge
for i in range (0,10):
    color = random.choice(['yellow', 'red', 'purple', 'black', 'blue', 'pink', 'green'])
    turtle.color(color)
    for i in range(0,8):
        turtle.forward(30)
        turtle.right(45)
    turtle.right(10)

#ninth challenge
lines = random.randint(5,20)

for i in range (0,lines):
    turtle.forward(random.randint(10,50))
    turtle.right(random.randint(10,500))


turtle.exitonclick()