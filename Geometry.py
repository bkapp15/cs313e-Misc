# File: Geometry.py

# Description: An exercise in object-oriented programming. This program contains geometry class definitions of point, line, and circle objects and various functions for the class objects. In main(), the file 'geometry.txt' is read in, variables are assigned to the contents and tests are run on the objects that are created based on them. The results of the tests are printed to console in sequential order.

# Student Name: Blake Kappel

# Student UT EID: bak792

# Course Name: CS 313E

# Unique Number: 51730

# Date Created: 2/9/15

# Date Last Modified: 2/14/15

##################################################################33

import math

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance to another Point object
  def dist (self, other):
    return math.hypot(self.x - other.x, self.y - other.y)

  # create a string representation of a Point (x, y)
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'
  
  # test for equality between two points
  def __eq__ (self, other):
    tol = 1.0e-18 # Some arbitrarily small number as tolerance
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Line (object):
  # constructor assign default values if user defined points are the same
  def __init__ (self, p1_x = 0, p1_y = 0, p2_x = 1, p2_y = 1):
    tol = 1.0e-18
    # Default case if the distance bwetween the two points is too small to be a line (arbitrary judgement)
    if ((abs(p1_x - p2_x) < tol) and (abs(p1_y - p2_y) < tol)):
      self.p1 = Point(0,0)
      self.p2 = Point(1,1)
    else:
      self.p1 = Point(p1_x, p1_y)
      self.p2 = Point (p2_x, p2_y)

  # determine if line is parallel to x axis
  def is_parallel_x (self):
    tol = 1.0e-18
    return (abs (self.p1.y - self.p2.y) < tol)

  # determine if line is parallel to y axis
  def is_parallel_y (self):
    tol = 1.0e-18
    return (abs(sel.p1.x - self.p2.x) < tol)

  # determine slope for the line
  # return float ('inf') if line is parallel to the y-axis
  def slope (self):
    tol = 1.0e-18
    if (abs(self.p1.x - self.p2.x) < tol):
      return float('inf')
    else:
      return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)

  # determine the y-intercept of the line
  def y_intercept (self):
    if self.slope() == float('inf'):
      return 'none'
    return (self.p1.y - (self.slope() * self.p1.x))
    
  # determine the x-intercept of the line
  def x_intercept (self):
    if self.slope() == 0:
      return 'none'
    elif self.slope() == float('inf'):
      return self.p1.x
    else:
      return (self.p1.y - (self.slope() * self.p1.x))

  # determine if two lines are parallel
  def is_parallel (self, other):
    tol = 1.0e-18
    return (abs (self.slope() - other.slope()) < tol)
    
  # determine if two lines are perpendicular to each other
  def is_perpendicular (self, other):
    tol = 1.0e-18
    return (self.slope() * other.slope() + 1) < tol

  # determine if a point is on the line or on an extension of it
  def is_on_line (self, p):
    tol = 1.0e-18
    check = (abs(p.y -(self.slope() * p.x - self.y_intercept())) < tol)
    return (check)
    if check == false:
      return abs(p.y - self.y)

  # determine the perpendicular distance of a point to the line
  def perp_dist (self, p):
    p_slope = -1/self.slope()
    p_y_int = p.y - (p_slope * p.x)
    pLine = Line (p.x, p.y, 0, p_y_int)
    intersectP = self.intersection_point(pLine)
    return p.dist(intersectP)

  # determine the intersection point of two lines if not parallel
  def intersection_point (self, other):
    x = (self.y_intercept() - other.y_intercept()) / (other.slope() - self.slope())
    return Point(x, (self.slope() * x + self.y_intercept()))

  # determine if two points are on the same side of the line
  # return False if one or both points are on the line
  def on_same_side (self, p1, p2):
    line_p1_y = self.slope() * p1.x + self.y_intercept()
    line_p2_y = self.slope() * p2.x + self.y_intercept()
    return ((p1.y < line_p1_y ) and (p2.y < line_p2_y)) or ((p1.y > line_p1_y) and (p2.y > line_p2_y))

  # string representation of the line - one of three cases
  # y = c
  # x = c
  # y = m * x + b
  def __str__ (self):
    if self.slope() == float('inf'):
      return 'x = ' + str(self.p1.x)
    elif self.slope() == 0:
      return 'y = ' + str(self.p1.y)
    else:
      if (self.y_intercept() > 0):
        return 'y = ' + str(self.slope()) + ' x + ' + str(self.y_intercept())
      elif (self.y_intercept() < 0):
        return 'y = ' + str(self.slope()) + ' x - ' + str(abs(self.y_intercept()))
      else:
        return ('y = ' + str(self.slope()) + ' x')
    
class Circle (object):
  # constructor with default values
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.center = Point(x,y)

  # compute circumference
  def circumference (self):
    return 2 * math.pi * self.radius

  # compute area
  def area (self):
    return math.pi * self.radius ** 2

  # determine if a point is inside the circle
  def is_inside_point (self, p):
    return (self.center.dist(p) < self.radius)

  # determine if the other circle is strictly inside self
  def is_inside_circle (self, other):
    distance = self.center.dist(other.center)
    return (distance + other.radius) < self.radius

  # determine if the other circle intersects self
  def does_intersect_circle (self, other):
    distance = self.center.dist(other.center)
    return (distance < (self.radius + other.radius))

  # determine if the line intersects circle
  def does_intersect_line (self, line):
    return (line.perp_dist(self.center) <= self.radius)

  # determine if the line is tangent to the circle
  def is_tangent (self, line):
    tol = 1.0e-18
    return (abs(line.perp_dist(self.center) - self.radius) < tol)

  # string representation of a circle
  # Radius: radius, Center: (x, y)
  def __str__ (self):
    return 'Radius: ' + str(self.radius) + ', Center: ' + str(self.center)

def main():

  # open file "geometry.txt" for reading
  inFile = open('geometry.txt', 'r')

  # read the coordinates of the first Point P
  line = inFile.readline()
  for i in range(len(line)):
    if (line[i : i+ 2] == '  '):
      line = line[0: i]
      break
  P_x, P_y = line.split(' ')
  P_x = float(P_x)
  P_y = float(P_y)
  P = Point(P_x, P_y)

  
  # read the coordinates of the second Point Q
  line = inFile.readline()
  for i in range(len(line)):
    if (line[i : i+ 2] == '  '):
      line = line[0: i]
      break
  Q_x, Q_y = line.split(' ')
  Q_x = float(Q_x)
  Q_y = float(Q_y)
  Q = Point(Q_x, Q_y)

  # print the coordinates of points P and Q
  print ('Coordinates of P: ' + str(P))
  print ('Coordinates of Q: ' + str(Q))

  # print distance between P and Q
  distance = P.dist(Q)
  print ('Distance between P and Q: ' + str(distance))

  # print the slope of the line PQ
  linePQ = Line(P.x, P.y, Q.x, Q.y)
  slopePQ = linePQ.slope()
  print ('Slope of PQ: ' + str(slopePQ))
  
  # print the y-intercept of the line PQ
  yIntPQ = linePQ.y_intercept()
  print ('Y-Intercept of PQ: ' + str(yIntPQ))

  # print the x-intercept of the line PQ
  xIntPQ = linePQ.x_intercept()
  print ('X-Intercept of PQ: ' + str(xIntPQ))

  # read the coordinates of the third Point A
  line = inFile.readline()
  for i in range(len(line)):
    if (line[i : i+ 2] == '  '):
      line = line[0: i]
      break
  A_x, A_y = line.split(' ')
  A_x, A_y = float(A_x), float(A_y)
  A = Point (A_x, A_y)
  
  # read the coordinates of the fourth Point B
  line = inFile.readline()
  for i in range(len(line)):
    if (line[i : i+ 2] == '  '):
      line = line[0: i]
      break
  B_x, B_y = line.split(' ')
  B_x, B_y = float(B_x), float(B_y)
  B = Point (B_x, B_y)
  
  # print the string representation of the line AB
  lineAB = Line(A.x, A.y, B.x, B.y)
  print ('Line AB: ' + str(lineAB))

  # print if the lines PQ and AB are parallel or not
  if linePQ.is_parallel(lineAB):
    par = 'is'
  else:
    par = 'is not'
  print ('PQ ' + par + ' parallel to AB')
  
  # print if the lines PQ and AB (or extensions) are perpendicular or not
  if linePQ.is_perpendicular(lineAB):
    per = 'is'
  else:
    per = 'is not'
  print ('PQ ' + per + ' perpendicular to AB')
  
  # print coordinates of the intersection point of PQ and AB if not parallel
  if not linePQ.is_parallel(lineAB):
    intP = linePQ.intersection_point(lineAB)
    print ('Intersection point of PQ and AB: ' + str(intP))

  # read the coordinates of the fifth Point G
  line = inFile.readline()
  for i in range(len(line)):
    if (line[i : i+ 2] == '  '):
      line = line[0: i]
      break
  G_x, G_y = line.split(' ')
  G_x = float(G_x)
  G_y = float(G_y)
  G = Point(G_x, G_y)

  # read the coordinates of the sixth Point H
  line = inFile.readline()
  for i in range(len(line)):
    if (line[i : i+ 2] == '  '):
      line = line[0: i]
      break
  H_x, H_y = line.split(' ')
  H_x = float(H_x)
  H_y = float(H_y)
  H = Point(H_x, H_y)

  # print if the the points G and H are on the same side of PQ
  if linePQ.on_same_side(G, H):
    ssPQ = 'are'
  else:
    ssPQ = 'are not'
  print ('G and H ' + ssPQ + ' on the same side of PQ')

  # print if the the points G and H are on the same side of AB
  if lineAB.on_same_side(G, H):
    ssAB = 'are'
  else:
    ssAB = 'are not'
  print ('G and H ' + ssAB + ' on the same side of AB')

  # read the radius of the circleA and the coordinates of its center
  line = inFile.readline()
  for i in range(len(line)):
    if (line[i : i+ 2] == '  '):
      line = line[0: i]
      break
  circleA_r, circleA_x, circleA_y = line.split(' ')
  circleA_r, circleA_x, circleA_y = float(circleA_r), float(circleA_x), float(circleA_y)
  circleA = Circle(circleA_r, circleA_x, circleA_y)
  
  # read the radius of the circleB and the coordinates of its center
  line = inFile.readline()
  for i in range(len(line)):
    if (line[i : i+ 2] == '  '):
      line = line[0: i]
      break
  circleB_r, circleB_x, circleB_y = line.split(' ')
  circleB_r, circleB_x, circleB_y = float(circleB_r), float(circleB_x), float(circleB_y)
  circleB = Circle(circleB_r, circleB_x, circleB_y)

  # print the string representation of circleA and circleB
  print ('circleA: ' + str(circleA))
  print ('circleB: ' + str(circleB))

  # determine if circleB is inside circleA
  if circleA.is_inside_circle(circleB):
    inside = 'is'
  else:
    inside = 'is not'
  print ('circleB ' + inside + ' inside circleA')

  # determine if circleA intersects circleB
  if circleB.does_intersect_circle(circleA):
    IntAns = 'does intersect'
  else:
    IntAns = 'does not intersect'
  print ('circleA ' + IntAns + ' circleB')

  # determine if line PQ (or extension) intersects circleA
  if circleA.does_intersect_line(linePQ):
    l_int = 'does intersect'
  else:
    l_int = 'does not intersect'
  print ('PQ ' + l_int + ' circleA')

  # determine if line AB (or extension) is tangent to circleB
  if circleB.is_tangent(lineAB):
    tan = 'is'
  else:
    tan = 'is not'
  print ('AB ' + tan + ' a tangent to circleB')

  # close file "geometry.txt"
  inFile.close()
  
main()