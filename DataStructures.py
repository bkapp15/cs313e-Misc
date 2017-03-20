# File Name: DataStructures.py

# Author: Blake Kappel

""" 
These are all the classes of data structure objects that were gone 
over during Mitra's CS313e class of the Spring 2015 semester. This file
was mad in an attempt to be able to import the classes from this file
into other programs
"""

"""==========================Stack Class=======================+"""
class Stack (object):
  def __init__ (self):
    self.stack = []

  # add an item to the top of the stack
  def push (self, item):
    self.stack.append ( item )

  # remove an item from the top of the stack
  def pop (self):
    return self.stack.pop()

  # check what item is on top of the stack without removing it
  def peek (self):
    return self.stack[len(self.stack) - 1]

  # check if a stack is empty
  def isEmpty (self):
    return (len(self.stack) == 0)

  # return the number of elements in the stack
  def size (self):
    return (len(self.stack))

"""========================Links and Linked Lists================="""
class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next
    
class LinkedList (object):

  # Constructor
  def __init__ (self):
    self.first = None

  # get number of links
  def getNumLinks (self):
        count = 0
        current = self.first
        while current != None:
          count += 1
          current = current.next
        return (count)

  # Add data at the beginning of the list
  def addFirst (self, data):
    newLink = Link(data)
    newLink.next = self.first
    self.first = newLink

  # Add data at the end of a list
  def addLast (self, data):
    newLink = Link (data) # Always have to make a new Link
    if self.isEmpty():
      self.first = newLink
      return

    current = self.first
    # Last link is when 'next = None'
    while (current.next != None):
      current = current.next
    current.next = newLink # Where the addition takes place

  # Add data in an ordered list in ascending order
  def addInOrder (self, data):
    newLink = Link(data)
    # If empty, assign newLink to first link
    if self.isEmpty():
      self.first = newLink
      return

    current = self.first
    previous = self.first
    # Making sure it iterates properly
    while (current.data <= newLink.data):
      previous = current
      current = current.next
      # If it reaches the end, add link to last position
      if (current == None):
        self.addLast(data)
        return
    # If the new link goes at the beginning
    if (current == self.first):
      self.addFirst(data)
      return
    # Where the addition of new link takes place
    previous.next = newLink
    newLink.next = current

  # Search in an unordered list, return None if not found
  def findUnordered (self, data):
    if self.isEmpty(): # If empty
      return None

    current = self.first
    while (current != None):
      if (current.data == data):
        return (current)
      current = current.next

    return current

  # Search in an ordered list, return None if not found
  def findOrdered (self, data):
    if self.isEmpty(): # If empty
      return None

    current = self.first
    while (current != None):
      if (current.data == data):
        return (current)
      current = current.next

    return current

  # Delete and return Link from an unordered list or None if not found
  def delete (self, data):
    if self.isEmpty(): # if empty
      return None

    current = self.first # start at beginning
    previous = self.first

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
        current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current # Return deleted link

  # String representation of data 10 items to a line, 2 spaces between data
  def __str__ (self):
    st = ''
    if self.isEmpty():
      return st
    st += str(self.first)
    current = self.first.next
    while (current != None):
      st += ('  ' + str(current))
      current = current.next
    return st

  # Copy the contents of a list and return new list
  def copyList (self):
    newLL = LinkedList()

    current = self.first
    while (current != None):
      newLL.addLast(current.data)
      current = current.next
    return newLL

  # Reverse the contents of a list and return new list
  def reverseList (self):
    newLL = LinkedList()
    newList = [] # Built in list object

    # Append to the regular list object
    current = self.first
    while (current != None):
      newList.append(current.data)
      current = current.next

    # Reversing by adding, item by item in regular list, to first position
    for item in newList:
      newLL.addFirst(item)
    return newLL

  # Sort the contents of a list in ascending order and return new list
  def sortList (self):
    newList = []
    newLL = LinkedList()

    current = self.first
    while (current != None):
      newList.append(current.data)
      current = current.next

    newList.sort()

    for item in newList:
      newLL.addLast(item)
    return newLL

  # Return True if a list is sorted in ascending order or False otherwise
  def isSorted (self):
    if self.isEmpty(): # if empty
      return True

    current = self.first
    previous = self.first
    while (current != None):
      if (previous.data > current.data):
        return False
      previous = current
      current = current.next
    return True

  # Return True if a list is empty or False otherwise
  def isEmpty (self):
    return (self.first == None)

  # Merge two sorted lists and return new list in ascending order
  def mergeList (self, b):
    currentA = self.first
    currentB = b.first
    c = LinkedList()
    while((currentA != None) and (currentB != None)):
      if(currentA.data < currentB.data):
        c.addLast(currentA.data)
        currentA = currentA.next
      else:
        c.addLast(currentB.data)
        currentB = currentB.next
    while(currentA != None):
      c.addLast(currentA.data)
      currentA = currentA.next
    while(currentB != None):
      c.addLast(currentB.data)
      currentB = currentB.next
    return c

  # Test if two lists are equal, item by item and return True
  def isEqual (self, b):
    # Make sure they are equal in length
    if (self.getNumLinks() != b.getNumLinks()):
      return False

    sCurrent = self.first
    bCurrent = b.first
    while (sCurrent != None):
      if (sCurrent.data != bCurrent.data):
        return False
      sCurrent = sCurrent.next
      bCurrent = bCurrent.next
    return True

  # Return a new list, keeping only the first occurence of an element
  # and removing all duplicates. Do not change the order of the elements.
  def removeDuplicates (self):
    newLL = LinkedList()
    checkList = []

    current = self.first
    while (current != None):
      if (current.data not in checkList):
        newLL.addLast(current.data)
        checkList.append(current.data)
      current = current.next
    return newLL

"""=======================Queue Class==========================="""
class Queue (object):
  def __init__ (self):
    self.queue = []

  def enqueue (self, item):
    self.queue.append (item)

  def dequeue (self):
    return (self.queue.pop(0))

  def isEmpty (self):
    return (len (self.queue) == 0)

  def size (self):
    return len (self.queue)

"""========================Node & Tree Classes==========================="""
class Node (object):
  # Constructor
  def __init__(self, data):
    self.data = data
    self.lChild = None
    self.rChild = None
   
  # String representations   
  def __str__(self):
    return str(self.data)
    
class BS_Tree (object):
  # Constructor
  def __init__(self):
    self.root = None
    
  # True if tree is empty
  def isEmpty(self):
    return self.root == None
    
  # Insert a node in a tree
  def insert (self, val):
    newNode = Node(val)
    if (self.isEmpty()):
      self.root = newNode
    else:
      current = self.root
      parent = self.root
      while (current != None):
        parent = current
        if (val < current.data):
          current = current.lChild
        else:
          current = current.rChild
      if (val < parent.data):
        parent.lChild = newNode
      else:
        parent.rChild = newNode
  
  # In-order traversal: left-center-right
  def inOrder(self, aNode, a): # a should be an empty list
    if (aNode != None):
      self.inOrder (aNode.lChild, a)
      a.append(aNode.data)
      self.inOrder (aNode.rChild, a)
      return a # By the end, a should be a list of all the data from the binary tree in ascending order
      
  # Pre-order traversal: center-left-right
  def preOrder(self, aNode):
    if (aNode != None):
      print (aNode.data)
      self.preOrder(aNode.lChild)
      self.preOrder(aNode.rChild)
      
  # Post-order traversal: left-right-center
  def postOrder(self, aNode):
    if (aNode != None):
      self.postOrder(aNode.lChild)
      self.postOrder(aNode.rChild)
      print(aNode.data)
  
  # Search for node with a given key
  def search (self, key):
    current = self.root
    while (current != None) and (current.data != key):
      if (key < current.data):
        current = current.lChild
      else:
        current = current.rChild
    return current

  # Returns true if two binary trees are similar
  def isSimilar (self, pNode):
    return (self.inOrder(self.root, []) == pNode.inOrder(pNode.root, []))
  
  # Prints out all nodes at the given level
  # Format: print all numbers in one line, numbers separated by a blank
  def printLevel (self, level): 
    # If empty
    if (self.isEmpty()):
      return
    
    # Utilizes Queue class to keep store the data in each level
    levelQ = Queue()
    levelQ.enqueue(self.root)
    levelStr = ''
    
    # Go through nodes, level by level
    for i in range(1, level):
      # Dequeue the parent node in order to enqueue to parent's children nodes
      for j in range(levelQ.size()):
        parent = levelQ.dequeue()
        if (parent.lChild != None) and (parent.rChild != None):
          levelQ.enqueue(parent.lChild)
          levelQ.enqueue(parent.rChild)
        elif (parent.lChild != None) and (parent.rChild == None):
          levelQ.enqueue(parent.lChild)
        elif (parent.lChild == None) and (parent.rChild != None):
          levelQ.enqueue(parent.rChild)
    
    
    lenQ = levelQ.size()
    # Increment onto the string to be printed
    for j in range(lenQ):
      levelStr += (str(levelQ.dequeue()) + ' ')
    levelStr = levelStr.strip()  
    print (levelStr)

  # Returns the height of the tree
  def getHeight (self): 
  
    # If empty
    if (self.isEmpty()):
      return 0
    
    count = -1
    current = self.root
    while (current != None):
      if (current.lChild != None):
        current = current.lChild
        count += 1
      else:
        current = current.rChild
        count += 1

    return max(count, self.helpheight())
    
  # Helper method for getHeight
  def helpheight(self):
    if (self.isEmpty()):
      return 0
    count = -1
    current = self.root
    while (current != None):
      if (current.rChild != None):
       current = current.rChild
       count += 1
      else:
        current = current.lChild
        count += 1
    return count

        
  # Returns the number of nodes in the left subtree and
  # the number of nodes in the right subtree
  def numNodes (self):
    # If empty
    if (self.isEmpty()):
      return None
      
    if (self.root.lChild != None) and (self.root.rChild != None):
      return len(self.inOrder(self.root.lChild, [])), len(self.inOrder(self.root.rChild, []))
    elif (self.root.lChild == None) and (self.root.rChild == None):
      return 0, 0
    elif (self.root.lChild == None) and (self.root.rChild != None):
      return 0, len(self.inOrder(self.root.rChild, []))
    elif (self.root.lChild != None) and (self.root.rChild == None):
      return len(self.inOrder(self.root.lChild, [])), 0


  # Find the node with the smallest value
  def minimum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.lChild
    return parent

  # Find the node with the largest value
  def maximum (self):
    current = self.root
    parent = current
    while (current != None):
      parent = current
      current = current.rChild
    return parent
      
""" Specific type of binary search tree used to encrypt and decrypt 
strings """
class CipherTree (object):
  # the init() function creates the binary search tree with the
  # encryption string. If the encryption string contains any
  # character other than the characters 'a' through 'z' or the
  # space character drop that character.
  def __init__ (self, encrypt_str):
    self.root = None
    chList = []
    for ch in encrypt_str:
      if (ch not in chList):
        chList.append(ch)
    for ch in chList:
      self.insert(ch)

  # the insert() function adds a node containing a character in
  # the binary search tree. If the character already exists, it
  # does not add that character. There are no duplicate characters
  # in the binary search tree.
  def insert (self, ch):
    newNode = Node(ch)
    if (self.root == None):
      self.root = newNode
      return
    current = self.root
    parent = self.root
    while (current != None):
      parent = current
      if (ch < current.data):
        current = current.lChild
      else:
        current = current.rChild
    if (ch < parent.data):
      parent.lChild = newNode
    else:
      parent.rChild = newNode

  # the search() function will search for a character in the binary
  # search tree and return a string containing a series of lefts
  # (<) and rights (>) needed to reach that character. It will
  # return a blank string if the character does not exist in the tree.
  # It will return * if the character is the root of the tree.
  def search (self, ch):
    if (ch == self.root.data):
      return '*'
    string = ''
    current = self.root
    while (current != None) and (current.data != ch):
      if (ch < current.data):
        string += '<'
        current = current.lChild
      else:
        string += '>'
        current = current.rChild
    if (current == None):
      return ''
    return string

  # the traverse() function will take string composed of a series of
  # lefts (<) and rights (>) and return the corresponding 
  # character in the binary search tree. It will return an empty string
  # if the input parameter does not lead to a valid character in the tree.
  def traverse (self, st):
    current = self.root
    if (st == '*'):
      return current.data
    for ch in st:
      if (ch == '<'):
        current = current.lChild
      if (ch == '>'):
        current = current.rChild
    return current.data

  # the encrypt() function will take a string as input parameter, convert
  # it to lower case, and return the encrypted string. It will ignore
  # all digits, punctuation marks, and special characters.
  def encrypt (self, st):
    string = ''
    for ch in st:
      string += self.search(ch) + '!'
    string = string[:len(string)-1]
    return string

  # the decrypt() function will take a string as input parameter, and
  # return the decrypted string.
  def decrypt (self, st):
    string = ''
    dirList = st.split('!')
    for dir in dirList:
      string += self.traverse(dir)
    return string
    
"""=========================Vertex & Graph Classes=========================="""
class Vertex(object):
  # Constructor
  def __init__(self, label):
    self.label = label
    self.visited = False
  
  # Determine if vertex was visited
  def wasVisited(self):
    return self.visited
  
  # Return label of vertex
  def getLabel(self):
    return self.label
    
  # String representation
  def __str__(self):
    return str(self.label)
    
  # Returns neighbors of vertex
  def getNeightbors(self):
    return # Needs to be developed
    

class Graph(object):
  
  # Constructor, graph consists of set V of Vertices and set E of Edges
  def __init__(self):
    self.Vertices = [] # List of the vertex objects being stored in the graph
    self.adjMat = [] # Adjacency matrix to represent weights, direction, positions
    
  # Check if a vertex label exists in the graph
  def hasVertex(self, label):
    nVert = len(self.Vertices) # number of vertices in the graph
    for i in range(nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False # If it goes thru list of vertices without matching any vertex label
  
  # Adds a vertex with a given label
  def addVertex(self, label):
    if not self.hasVertex(label): # Only adds if vertex does not already exist
      self.Vertices.append(Vertex(label))
      # Add a new column in adjMat for new vertex
      nVert = len(self.Vertices)
      for i in range (nVert - 1): # B/c new row hasn't been added
        (self.adjMat[i]).append(0)
        # Add a new row in adjMat for new vertex
        newRow = []
        for i in range(nVert):
          newRow.append(0)
        self.adjMat.append(newRow)
        
  # Return an unvisited vertex adjacent to v
  def getAdjUnvisitedVertex(self, v):
    nVert = len(self.Vertices)
    for i in range(nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1
        
  # Add weighted, undirected edge to graph
  def addUndirectedEdge(self, start, finish, wight = 1):
    # Edge is represented in two positions on the graph b/c it is 
    # undirected
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight
    
  # Does a depth first search (dfs) in a graph, with v as starting vertex
  def dfs(self, v):
    # Create a stack object, would need to import
    theStack = Stack()
    
    # Mark visited vertices as visited and push onto stack
    (self.Vertices[v]).visited = True
    theStack.push[v]
    print (self.Vertices[v])
    while (not theStack.isEmpty()):
      # Get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex(theStack.peek())
      if (u == -1):
        u = theStack.pop()
      else:
        (self.Vertices[u]).visited = True
        theStack.push(u)
        print (self.Vertices[u])
  
    # Stack is empty, reset the flags
    nVert = len(self.Vertices)
    for i in range(nVert):
      (self.Vertices[i]).visited = False
      
  # Does a breadth first search (bfs) in a graph, with v as starting vertex
  def bfs(self, v):
    # Create a queue object
    theQ = Queue()
    # Mark the vertex as visited and enqueue
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theQ.enqueue(v)
    while not theQ.isEmpty():
      # Get the vertex at front
      v1 = theQ.dequeue()
      # Get an adjacent unvisited vertex
      v2 = self.getAdjUnvisitedVertex(v1)
      while (v2 != -1):
        (self.Vertices[v2]).visited = True
        print (self.Vertices[v2])
        theQ.enqueue(v2)
        v2 = self.getAdjUnvisitedVertex(v1)
    # Queue is empty, reset flags
    nVert = len(self.Vertices)
    for i in rang(nVert):
      (self.Vertices[i]).visited = False
      
"""=============Matrix Link and Matrix Objects and methods================="""
class matLink (object):
  def __init__ (self, row, col, data, next = None):
    self.row = row
    self.col = col
    self.data = data
    self.next = next

class SparseMatrix (object):
  def __init__ (self, row = 0, col = 0):
    self.num_rows = row      # number of rows
    self.num_cols = col      # number of columns
    self.matrix = None

  def insertLink (self, row, col, data):
    # do nothing if data = 0
    if (data == 0):
      return

    # create new link
    newLink = matLink (row, col, data)

    # if matrix is empty then the newLink is the first link
    if (self.matrix == None):
      self.matrix = newLink
      return

    # find position to insert
    previous = self.matrix
    current = self.matrix

    while ((current != None) and (current.row < row)):
      previous = current
      current = current.next

    # if the row is missing
    if ((current != None) and (current.row > row)):
      previous.next = newLink
      newLink.next = current
      return

    # on the row, search by column
    while ((current != None) and (current.col < col)):
      previous = current
      current = current.next

    # if link already there do not insert but reset data
    if ((current != None) and (current.row == row) and (current.col == col)):
      current.data = data
      return

    # now insert newLink
    previous.next = newLink
    newLink.next = current

    # Change self.num_rows and self.num_cols
    current = self.matrix
    max_col = 0
    while (current.next != None):
      current = current.next
      if (current.col > max_col):
        max_col = current.col

    self.num_rows = current.row + 1
    self.num_cols = max_col + 1

  # return a row of the sparse matrix
  def getRow(self, row_num):
    # create a blank list
    a = []

    # search for the row
    current = self.matrix
    if current == None:
      return a

    while (current != None) and (current.row < row_num):
      current = current.next

    # If the row is not represented in linked list because they're all 0s
    if (current != None) and (current.row > row_num):
      for i in range(self.num_cols):
        a.append(0)

    # Found the row
    if (current != None) and (current.row == row_num):
      # Takes care of all possibilities
      for j in range(self.num_cols):
        if (current.col == j) and (current.next != None):
          a.append(current.data)
          current = current.next
        elif (current.col == j) and (current.next == None):
          a.append(current.data)
        else:
          a.append(0)

    if (current == None) and (row_num < self.num_rows) and (a == []):
      for j in range(self.num_cols):
        a.append(0)

    return a

  # returns a column of the sparse matrix
  def getCol (self, col_num):
    # Create empty list to store column data
    a = []

    if (self.matrix == None) or (self.num_cols < col_num):
      return a

    # Loops through each row and uses getRow method to
    for i in range(self.num_rows):
      row = self.getRow(i)
      a.append(row[col_num])

    return a

  # adds two sparse matrices
  def __add__ (self, other):
    # Check if dimensions are equal
    if (self.num_rows != other.num_rows) or (self.num_cols != other.num_cols):
      return

    newMatrix = SparseMatrix()
    for i in range(self.num_rows):
      sRow = self.getRow(i)
      oRow = other.getRow(i)
      for j in range(len(sRow)):
        data = sRow[j] + oRow[j]
        newMatrix.insertLink(i, j, data)
    return newMatrix

  # multiplies two sparse matrices
  def __mul__ (self, other):
    if (self.num_cols != other.num_rows):
      return

    newMatrix = SparseMatrix()
    for i in range(self.num_rows):
      sRow = self.getRow(i)
      for j in range(other.num_cols):
        oCol = other.getCol(j)
        multSum = 0
        for k in range(len(sRow)):
          multSum += sRow[k] * oCol[k]
        newMatrix.insertLink(i, j, multSum)
    return newMatrix


  # returns a string representation of a matrix
  def __str__ (self):
    s = ''
    current = self.matrix

    # if the matrix is empty return blank string
    if (current == None):
      return s

    for i in range (self.num_rows):
      for j in range (self.num_cols):
        if ((current != None) and (current.row == i) and (current.col == j)):
          s = s + str (current.data) + " "
          current = current.next
        else:
          s = s + "0 "
      s = s + "\n"

    return s
