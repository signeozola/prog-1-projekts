##import turtle
##elsa = turtle.Turtle()
##for i in range(4):
##    elsa.forward(100)
##    elsa.right(90)

import turtle
import random
elsa = turtle.Turtle()
turtle.Screen().bgcolor("grey")
colours = ["cyan", "purple", "white", "blue"]

elsa.penup()
elsa.forward(90)
elsa.left(45)
elsa.pendown()

def branch():
  for i in range(3):
    for i in range(3):
        elsa.forward(30)
        elsa.backward(30)
        elsa.right(45)
    elsa.left(90)
    elsa.backward(30)
    elsa.left(45)
  elsa.right(90)
  elsa.forward(90)
       
for i in range(8):
  branch()
  elsa.left(45)
      #elsa.color(random.choice(colours))

##import turtle
##import random
##elsa = turtle.Turtle()
##turtle.Screen().bgcolor("grey")
##colours = ["cyan", "purple", "white", "blue"]
##elsa.color("cyan")
##for i in range(10):
##    for i in range(2):
##     elsa.forward(100)
##     elsa.right(60)
##     elsa.forward(100)
##     elsa.right(120)
##    elsa.right(36)
##    elsa.color(random.choice(colours))
