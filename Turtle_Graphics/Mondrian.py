#  File: Mondrian.py

#  Description: This was a pretty cool program assignment. Essentially, it creates a Mondrian-type painting using recursion and randomness. (There's a little haiku at the end.)

#  Student Name: Blake Kappel

#  Student UT EID: bak792

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 3/2/2015

#  Date Last Modified: 3/7/2015

####################################################

import turtle, random

# Returns random position from where the line will be drawn
def randomPos(lo, hi):
  return random.randint(lo, hi)

# Random decision, whether to draw a line or not, probability increases as recursion level increases
def noLine(count):
  num = random.randint(2,10)
  return (num in range(count + 1))

# Random decision, whether to use color or not, probability is higher for higher recursion levels
def useColor(count):
  if count < 3:
    num = random.randint(0, 6)
  else:
    num = random.randint(1, 10)
  return (num in range(count + 1))
  
# Random color to use to fill spaces
def randomColor():
  # Each possible letter choice corresponds to a color in this dictionary
  colorDict = {'r': 'red', 'y': 'yellow', 'g': 'gray', 'b': 'blue', 'z': 'black'}
  col = random.choice('rygbz')
  return colorDict[col]
  
def thickness(count):
  return 8 - count
    
# Draw a line from point p1 to point p2, used in drawRect function
def drawLine (ttl, p1, p2):
  x1 = p1[0]
  y1 = p1[1]
  x2 = p2[0]
  y2 = p2[1]
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

# Testing this function to see if it get the filling with color to work
def drawRect(ttl, p1, p2, p3, p4, counter):
  # Default white fill color
  ttl.fillcolor('white')
  # Random fill color if color is used
  if useColor(counter):
    color = randomColor()
    ttl.fillcolor(color)
  # Draws the rectangle with the set fill color
  ttl.begin_fill()
  drawLine(ttl, p1, p2)
  drawLine(ttl, p2, p3)
  drawLine(ttl, p3, p4)
  drawLine(ttl, p4, p1)
  # This is needed
  ttl.end_fill()
  
# Function that draws a mimicked Mondrian painting using random and recursion
def mimicMondrian(ttl, order, loX, hiX, loY, hiY, counter):
  
  # The canvases can't be too small and unsubstantial
  if (hiX - loX < 20) or (hiY - loY < 20):
    return
  
  # The masterpiece is complete once order reaches 0
  if order > 0:
    
    # Draw line or nah?
    if not noLine(counter):
      
      # Random direction, h for horizontal, v for vertical
      dir = random.choice('hv')
      ttl.pensize(thickness(counter))
      
      # Horizontal
      if (dir == 'h'):
      
        # Random placement of line
        randomY = randomPos(loY + 10, hiY - 10)
        # All points needed to draw the rectangles, based on random position
        p1 = [loX, randomY] 
        p2 = [hiX, randomY] 
        p3 = [hiX, hiY]
        p4 = [loX, hiY]
        p5 = [hiX, loY]
        p6 = [loX, loY]

        # Draw these bad boys        
        drawRect(ttl, p1, p2, p3, p4, counter)
        drawRect(ttl, p1, p2, p5, p6, counter)
        
        # Two recursive calls to account for upper and lower canvases that were created
        mimicMondrian(ttl, order - 1, loX, hiX, randomY, hiY, counter + 1)
        mimicMondrian(ttl, order - 1, loX, hiX, loY, randomY, counter + 1)
        
      # Vertical
      elif (dir == 'v'):
        # Random line placement
        randomX = randomPos(loX + 10, hiX - 10)
        # All points to be used in the drawRect function calls
        p1 = [randomX, loY] 
        p2 = [randomX, hiY] 
        p3 = [hiX, hiY]
        p4 = [hiX, loY]
        p5 = [loX, hiY]
        p6 = [loX, loY]
        
        # Divide into two canvases
        drawRect(ttl, p1, p2, p3, p4, counter)
        drawRect(ttl, p1, p2, p5, p6, counter)
        
        # Recursive call for right canvas
        mimicMondrian(ttl, order - 1, randomX, hiX, loY, hiY, counter + 1)
        # Recursive call for left canvas
        mimicMondrian(ttl, order - 1, loX, randomX, loY, hiY, counter + 1)
      

def main():
  
  # Output
  print ('Mondrian Composition\n')
  level = int(input("Enter a level of recursion between 1 and 6: "))
  
  # Invalid input statement
  if (level < 0) or (level > 6):
    print ('Invalid Input')
    return
  
  # Prep work for turtle drawing
  turtle.setup(800, 800, 0, 0)
  turtle.title("You're experience Mondrian-style painting like never before!")
  ttl = turtle.Turtle()
  ttl.shape('turtle')
  ttl.speed(0)
  #ttl.pensize(5)
  ttl.hideturtle()
  
  # Recursive function call
  count = 0
  mimicMondrian(ttl, level, -400, 400, -400, 375, count)
  
  # Haiku, because I just can't help from creatively expressing myself.
  hiY = randomPos(0,300)
  midY = randomPos(-200, hiY -50)
  loY = randomPos(-350, midY - 50)
  ttl.pencolor('orange')
  ttl.goto(randomPos(-400,150), hiY)
  ttl.write('Truly beautiful', False, 'left', ('Arial', 15, 'italic'))
  ttl.goto(randomPos(-400,150), midY)
  ttl.write('Code making beautiful art', False, 'left', ('Arial', 15, 'italic'))
  ttl.goto(randomPos(-400,150), loY)
  ttl.write('Oh how beautiful', False, 'left', ('Arial', 15, 'italic'))
  
  # Saves image as a .eps file
  ts = turtle.getscreen()
  ts.getcanvas().postscript(file = 'Mondrian.jpg')
  turtle.hideturtle()
  turtle.done()

main()
  
