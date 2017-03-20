#  File: Boxes.py

#  Description: This program determines the largest nestable set of boxes given n number of box dimensions. It utilizes a recursive subsets function, and appends nestable subsets of the box dimensions to a list, and outputs the nestable subsets that match the maximum length.

#  Student Name: Blake Kappel

#  Student UT EID: bak792

#  Partner Name: Jacob Martinez

#  Partner UT EID: jam22426

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 2/25/2015

#  Date Last Modified: 2/28/2015

#################################################################################

# Given dimensions of box a and box b in a list, tests whether box a can nest inside box b
def can_nest(a, b):
  return a[0] < b[0] and a[1] < b[1] and a[2] < b[2]

# Determines nest-ability of whole list of boxes, given that the list is sorted already
def can_nest_all(subset):
  for i in range(0, len(subset) -1):
    if not can_nest(subset[i], subset[i + 1]):
      return False
  return True
  
# Variation of standard subsets function in that this only appends subsets that fit the nestable condition
def subsets (a, b, lo, nest_subs):
  hi = len(a)
  if (lo == hi):
    # Nestable condition before appending
    if can_nest_all(b):
      nest_subs.append(b)
      return
  else:
    c = b[:]
    b.append (a[lo])
    subsets (a, c, lo + 1, nest_subs)
    subsets (a, b, lo + 1, nest_subs)

def main():
  
  # Opens boxes.txt file for reading
  infile = open ('boxes.txt', 'r')
  # Assigns first line to n, and converts to int
  n = int(infile.readline())
  
  # Case where n is not valid
  if (n <= 0):
    print ('Invalid number given for boxes')
    return
  
  # Will append all nestable subsets of all_boxes
  allsubs = []
  # 2D list that will contain all box dimension lists  
  all_boxes = [] 
  
  # For each other line, creates list dim_set out of 3 given dimensions, appends dim_set list to all_boxes list 
  # Try-except clause used in case ValueError arises; if so, will print error statement and end main()
  try:
    for i in range (0, n):
      box = infile.readline()
      box = box.strip()
      dim1, dim2, dim3 = box.split(" ")
      dim1, dim2, dim3 = int(dim1), int(dim2), int(dim3)
      dim_set = [dim1, dim2, dim3]
      dim_set.sort()
      all_boxes.append(dim_set)
  except ValueError:
    print('Invalid Content Values')
    return
  
  # All contents read in, time to close this baby
  infile.close()
  
  # Sorts all_boxes to ensure that they're in correct order to run can_nest_all function on them
  all_boxes.sort()

  # Empty list to satisfy parameter in of subsets function
  empty = []
  subsets(all_boxes, empty, 0, allsubs)
  
  # Initialize max size tracker as 2 because that's the minumum
  max_size = 2
  # Determines max_size
  for sub in allsubs:
  	if len(sub) > max_size:
  	  max_size = len(sub)

  # Subsets to trash if they are not of the max_size
  trash = []
  for i in range(0, len(allsubs)):
  	if len(allsubs[i]) != max_size:
  		trash.append(allsubs[i])

  # Removes trashable subsets , after which only subsets of max_size should be in allsubs
  for sub in trash:
  	allsubs.remove(sub)
  
  # Prep sort to meet output standard
  allsubs.sort()
  
  # Specifically formatted output
  print ("Largest Subset of Nesting Boxes")
  for sub in allsubs:
    for box in sub:
      print (box)
    print('')
 
"""  for i in range(len(allsubs)):
    for j in range(len(allsubs[i])):
      print (allsubs[i][j])
    if (i < len(allsubs) - 1):
      print('')"""
      
main()