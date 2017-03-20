#  File: Train.py

#  Description: Using the tools that come with the turtle graphics package, this program draws a fairly detailed train

#  Student Name: Blake Kappel

#  Student UT EID: bak792

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 2/20/2015

#  Date Last Modified: 2/21/2015

########################################################################

import turtle, math

# Draws a line, give 2 sets coordinates
def drawLine (ttl, x1, y1, x2, y2):
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

# Differs from drawRectangle by filling in the shape with color
def fillRectangle (ttl, x, y, side1, side2):
  ttl.penup()
  ttl.goto(x, y)
  ttl.begin_fill()
  ttl.pendown()
  ttl.forward(side1)
  ttl.right(90)
  ttl.forward(side2)
  ttl.right(90)
  ttl.forward(side1)
  ttl.right(90)
  ttl.forward(side2)
  ttl.right(90)
  ttl.end_fill()

# Draws rectangle
def drawRectangle (ttl, x, y, side1, side2):
  ttl.penup()
  ttl.goto(x, y)
  ttl.pendown()
  ttl.forward(side1)
  ttl.right(90)
  ttl.forward(side2)
  ttl.right(90)
  ttl.forward(side1)
  ttl.right(90)
  ttl.forward(side2)
  ttl.right(90)

# Train tracks function
def drawTracks(ttl, x = -350, y = -300, length = 700, numNotch = 13, lenNotch = 30, widNotch = 5):
  ttl.penup()
  ttl.goto(x, y)
  ttl.pendown()
  ttl.fd(length)
  ttl.penup()
  ttl.goto(x, y - 20)
  ttl.pendown()
  ttl.fd(length)
  inc = length // numNotch
  for i in range (numNotch):
    drawRectangle(ttl, (x + 10) + (i * inc), y - 20, lenNotch, widNotch)

# Draws the wheels
def drawWheel(ttl, x, y, outRadius, midRadius, inRadius):
  ttl.penup()
  ttl.goto(x, y)
  ttl.pendown()
  ttl.circle(outRadius)
  ttl.penup()
  ttl.goto(x, y + (outRadius - midRadius))
  ttl.pendown()
  ttl.circle(midRadius)
  ttl.penup()
  ttl.goto(x, y + (outRadius - inRadius))
  xCor, yCor = ttl.xcor(), ttl.ycor() # x and y for spokes later
  ttl.pendown()
  ttl.circle(inRadius)
  ttl.penup()

  # Spokes
  length = midRadius - inRadius
  angle = 0
  while (angle < 360):
    ttl.penup()
    ttl.goto(xCor, yCor)
    # first line
    ttl.right(85)
    ttl.pendown()
    ttl.fd(length)
    # second line
    ttl.penup()
    ttl.goto(xCor, yCor)
    ttl.right(10)
    ttl.pendown()
    ttl.fd(length)
    # 45 degree circle segment
    ttl.penup()
    ttl.goto(xCor,yCor)
    ttl.left(95)
    ttl.circle(inRadius, 45)
    xCor, yCor = ttl.xcor(), ttl.ycor()
    angle += 45

# Draws cab part of train
def drawCab(ttl, x, y, wheelRadius):
  ttl.penup()
  ttl.goto(x, y)
  ttl.pendown()
  width = wheelRadius * 2 + wheelRadius
  ttl.forward(width)
  ttl.right(90)
  ttl.fd(325)
  inc = wheelRadius // 2 - 5
  ttl.right(90)
  ttl.fd(inc)
  ttl.right(90)
  ttl.circle(wheelRadius + (inc//2), 180,)
  ttl.right(90)
  ttl.fd(inc)
  ttl.right(90)
  ttl.fd(325)
  ttl.right(90)
  ttl.fd(25)

  # Windows and top part of cab
  drawRectangle(ttl, ttl.xcor() -50, ttl.ycor() + 10, width + 75, 10)
  ttl.fillcolor('gray')
  fillRectangle(ttl, ttl.xcor() +50, ttl.ycor() - 30, 75, 100)
  fillRectangle(ttl, ttl.xcor() + 100, ttl.ycor(), 75, 100)

# Main body of train
def drawBody(ttl, x, y, wheelRadius):
  ttl.penup()
  ttl.goto(x, y)
  ttl.pendown()
  length = wheelRadius * 4 + 130
  ttl.forward(length)
  ttl.right(90)
  ttl.fd(275)
  inc = wheelRadius // 2 - 5
  ttl.right(90)
  ttl.fd(inc)
  ttl.right(90)
  ttl.circle(wheelRadius + (inc//2), 180,)
  ttl.right(90)
  ttl.fd(inc)
  ttl.right(90)
  ttl.circle(wheelRadius + (inc//2), 180)
  ttl.right(90)
  ttl.fd(inc)
  ttl.right(90)
  ttl.fd(275)
  ttl.right(90)
  ttl.fd(25)

# Draws rivets using dot built-infunction, horizontally 
def drawRivetsHorizontal(ttl, x, y, limit, space):
  length = 0
  while (length < limit):
    length += space
    x += space
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.dot(8, 'black')

# Draws rivets vertically
def drawRivetsVertical(ttl, x, y, limit, space):
  length = 0
  while (length < limit):
    length += space
    y += space
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.dot(8, 'black')

# Draws a 4-point figure, used for trapezoid figures
def drawTrap(ttl, x1, y1, x2, y2, x3, y3, x4, y4):
  ttl.penup()
  ttl.goto(x1, y1)
  drawLine(ttl, x1, y1, x2, y2)
  drawLine(ttl, x2, y2, x3, y3)
  drawLine(ttl, x3, y3, x4, y4)
  drawLine(ttl, x4, y4, x1, y1)

def main():
  
  turtle.title('Choo-choo')
  turtle.setup(800, 800, 0, 0)
  ttl = turtle.Turtle()
  ttl.speed(0)
  ttl.pensize(3)
  
  drawTracks(ttl, -350, -200, 700)

  ttl.color('red')
  drawWheel(ttl, -250, -200, 75, 55, 10)
  drawWheel(ttl, -13, -200, 70, 50, 9)
  drawWheel(ttl, 190, -200, 70, 50, 9)

  ttl.color('blue')
  drawCab(ttl, -350, 200, 75)

  drawBody(ttl, -105, 150, 70)

  drawRectangle(ttl, -25, 170, 75, 20)
  drawRectangle(ttl, -10, 180, 45, 10)

  drawRectangle(ttl, 305, 100, 20, 100)
  drawRectangle(ttl, 325, 75, 10, 50)

  drawLine(ttl, -130, 25, 305, 25)
  drawLine(ttl, -130, 5, 305, 5)

  drawRivetsHorizontal(ttl, -130, 15, 425, 10)

  drawLine(ttl, -30, 150, -30, 25)
  drawLine(ttl, -50, 150, -50, 25)

  drawRivetsVertical(ttl, -40, 25, 115, 10)

  drawLine(ttl, 180, 150, 180, 25)
  drawLine(ttl, 200, 150, 200, 25)

  drawRivetsVertical(ttl, 190, 25, 115, 10)

  drawTrap(ttl, 305, -100, 355, -100, 380, -150, 305, -150)
  drawTrap(ttl, 170, 150, 150, 250, 230, 250, 210, 150)
  drawTrap(ttl, 150, 250, 160, 275, 220, 275, 230, 250)
  
  turtle.done()

main()
