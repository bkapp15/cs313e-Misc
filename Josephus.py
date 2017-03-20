#  File: Josephus.py

#  Description: Using circular linked lists, simulate the Josephus problem. 

#  Student Name: Blake Kappel

#  Student UT EID: bak792

#  Partner Name: Jacob Martinez

#  Partner UT EID: jam22426

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 3/30/2015

#  Date Last Modified: 4/4/2015


############################################################################

# Link objects will be used throughout the code, where in main each link represents a soldier
class Link(object):
  def __init__ (self, item, next = None):
    self.data = item  # information (number of soldier) as data element of link
    self.next = next  # The actual link element

# CircularList class has methods insert, find, delete, etc.
class CircularList(object):
  # Constructor
  def __init__ (self):
    self.first = None  # Only need to create object of data, not link. Links will be made in insert function

  # Insert an element in the last position of the circular list
  def insert (self, item):
    # Creates the link to be inserted at the end of list using item as data component and self.first as next address, making it circular
    newLink = Link (item, self.first)
    current = self.first
    # If list is empty
    if (current == None):
      self.first = newLink # create a new link if self.first is equal to None
      self.first.next = self.first # make self.first.next equal to self.first so that if it is also equal to None, and it's space can be filled with '2'
      return # after self.first.next is also found to be 'None', it will add '2'
 
    # For a non-empty list, reaches last link in list
    while (current.next != self.first):
      current = current.next
    # After reaching last link
    current.next = newLink # Assigns next of last link to the newLink

  # Find the link with the given key
  def find (self, key):
    current = self.first

    if (current.next == None): # checks if data exists
      return None # if list is empty, nothing to return
    
    # If the key is found, loop terminates with current.data == key
    while (current.data != key):
      current = current.next
    
    # Returns what is found
    return current # 'pointer', address of link, returns the object that houses the data of the item being found

  # Delete a link that has given key as its data
  def delete (self, key):
    current = self.first # start at beginning
    previous = self.first

    # Goes through list until key is found
    while (current.data != key):
        previous = current
        current = current.next

    # Special circumstance if self consists of only one link, self.first
    if (current == self.first):
      self.atlastLink() # needs to return current.next = self.first.next
      self.first = self.first.next ## This ensures that the 'None' values initialized with self do not disrupt the count of soldiers.
    # Otherwise, link is deleted by simply skipping the current link
    else:
      previous.next = current.next

    return current.data # link I wanted to delete  

  # Delete the nth link starting from the Link start 
  # Returns the deleted link data and the new start element
  def deleteAfter (self, start, n):
    current = self.find(start) # starts from start
      
    for count in range (0, n-1): # n -1 because current is also counted... current (1), 2, deletedcurrent (3) in cases where n = 3 for example
      current = current.next
    # Changed from print to storing the data, so that it can be utilized in main
    dead = self.delete(current.data)

    # Returns the new start, no longer contains dead
    return (dead, current.next.data) # data value after previous link has been deletedt loop can continue

  # Return a string representation of a Circular List
  # Format: simply the each link's data with spaced in between
  def __str__ (self):
    st = ''
    current = self.first.next
    while (current.next != self.first):
      st += (str(current.data) + ' ')
      current = current.next
    st += (str(current.data) + ' ')
    return (st)

  # checks where or not we are at the last link in the list, if we are, we need to skip over current.next (where self.first == None)
  def atlastLink(self):  
    current = self.first
    while(current.next != self.first):
      current = current.next

    current.next = self.first.next
    return
  
  # Length function used to check whether links were being deleted (reattached) properly
  def length (self):
    count = 0
    current = self.first

    while (current.next != self.first):
      current = current.next
      count += 1 
    return (count)   


    

def main():

  # Open this file to gather the input
  infile = open ('josephus.txt', 'r')
  
  # Assigns the variables and converts to int for each one
  # sold (number of soldiers, star (the soldier's number from which to start the count), n (the count)  sold = infile.readline()
  sold = infile.readline()
  sold = int(sold.strip())
  start = infile.readline()
  start = int(start.strip())
  n = infile.readline()
  n = int(n.strip())
  
  circle = CircularList() # intialize the circle object
  
  # inserting the soldier numbers in to the list
  for i in range (1, sold + 1):
    circle.insert(i)

  # Initialize output string
  outStr = ''
  # Loop where all the work is done
  for j in range (1, sold + 1): 
    dead, start = circle.deleteAfter(start, n) # Iterate through links, returning the new starting point at current.next.data (after current.data has been deleted)
    outStr += (str(dead) + ' ') # Adds the stuff to the string to be finally outputted
    
  # Finally, here, it's supposed to output the number of soldiers in the order that they were killed off
  print (outStr)
    
main()
