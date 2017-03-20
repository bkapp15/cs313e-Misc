#  File: Graph.py

#  Description: Demonstrating methods of the graph class: dfs, bfs, topological sorting, sorting edges by weight, and single source shortest path.

#  Student Name: Blake Kappel

#  Student UT EID: bak792

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 4/30/2015

#  Date Last Modified: 5/7/2015

#####################################################


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

class Vertex (object):
  def __init__ (self, label):
    self.label = label
    self.visited = False

  # determine if vertex was visited
  def wasVisited (self):
    return self.visited 

  # determine the label of the vertex
  def getLabel (self):
    return self.label

  # string representation of the label
  def __str__(self):
    return str (self.label)

class Edge (object):
  def __init__ (self, fromVertex, toVertex, weight):
    self.u = fromVertex
    self.v = toVertex
    self.weight = weight

  # comparison operators
  def __lt__ (self, other):
    if (self.weight < other.weight):
      return True
    else:
      return False

  def __le__ (self, other):
    if (self.weight <= other.weight):
      return True
    else:
      return False

  def __gt__ (self, other):
    if (self.weight > other.weight):
      return True
    else:
      return False

  def __ge__ (self, other):
    if (self.weight >= other.weight):
      return True
    else:
      return False

  def __eq__ (self, other):
    if (self.weight == other.weight):
      return True
    else:
      return False

  def __ne__ (self, other):
    if (self.weight != other.weight):
      return True
    else:
      return False
  
class Graph (object):
  def __init__ (self):
    self.Vertices = []
    self.Edges = []
    self.adjMat = []

  # Resets the visited flags for every vertex in self.Vertices 
  def resetVisited(self):
    nVert = len (self.Vertices)
    for i in range (nVert):
      (self.Vertices[i]).visited = False
  
  # checks if a vertex label already exists
  def hasVertex (self, label):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (label == (self.Vertices[i]).label):
        return True
    return False

  # add a vertex with given label
  def addVertex (self, label):
    if not self.hasVertex (label):
      self.Vertices.append (Vertex (label))

      # add a new column in the adjacency matrix for new Vertex
      nVert = len (self.Vertices)
      for i in range (nVert - 1):
        (self.adjMat[i]).append (0)
    
      # add a new row for the new Vertex in the adjacency matrix
      newRow = []
      for i in range (nVert):
        newRow.append (0)
      self.adjMat.append (newRow)

  # add weighted directed edge to graph
  def addDirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    # Also add Edge object to Edges list
    edge = Edge(self.Vertices[start], self.Vertices[finish], weight)
    self.Edges.append(edge)

  # add weighted undirected edge to graph
  def addUndirectedEdge (self, start, finish, weight = 1):
    self.adjMat[start][finish] = weight
    self.adjMat[finish][start] = weight
    # Also add two new edges to Edges list
    edge1 = Edge(self.Vertices[start], self.Vertices[finish], weight)
    edge2 = Edge(self.Vertices[finish], self.Vertices[start], weight)
    self.Edges.append(edge1)
    self.Edges.append(edge2)

  # return an unvisited vertex adjacent to v
  def getAdjUnvisitedVertex (self, v):
    nVert = len (self.Vertices)
    for i in range (nVert):
      if (self.adjMat[v][i] > 0) and (not (self.Vertices[i]).wasVisited()):
        return i
    return -1

  # does a depth first search in a graph
  def dfs (self, v):
    # create a stack
    theStack = Stack()

    # mark the vertex as visited and push on the stack
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theStack.push (v)

    while (not theStack.isEmpty()):
      # get an adjacent unvisited vertex
      u = self.getAdjUnvisitedVertex (theStack.peek())
      if (u == -1):
        u = theStack.pop() 
      else:
        (self.Vertices[u]).visited = True
        print (self.Vertices[u])
        theStack.push(u)

    # stack is empty reset the flags
    self.resetVisited()

  # does a breadth first search in a graph
  def bfs (self, v):
    # create a queue
    theQueue = Queue ()

    # mark the vertex as visited and enqueue
    (self.Vertices[v]).visited = True
    print (self.Vertices[v])
    theQueue.enqueue (v)

    while (not theQueue.isEmpty()):
      # get the vertex at the front
      v1 = theQueue.dequeue()
      # get an adjacent unvisited vertex
      v2 = self.getAdjUnvisitedVertex (v1)
      while (v2 != -1):
        (self.Vertices[v2]).visited = True
        print (self.Vertices[v2])
        theQueue.enqueue (v2)
        v2 = self.getAdjUnvisitedVertex (v1)

    # queue is empty reset the flags
    self.resetVisited()
      
  # get index from vertex label
  def getIndex (self, label):
    for i in range(len(self.Vertices)):
      if ((self.Vertices[i]).label == label):
        return i

  # get edge weight between two vertices
  # return -1 if edge does not exist
  def getEdgeWeight (self, fromVertexLabel, toVertexLabel):
    i = self.getIndex(fromVertexLabel)
    j = self.getIndex(toVertexLabel)
    if (self.adjMat[i][j] != 0):
      return self.adjMat[i][j]
    return -1

  # get a list of neighbors that you can go to from a vertex
  # return empty list if there are none
  def getNeighbors (self, vertexLabel):
    nList = []
    idx = self.getIndex(vertexLabel)
    for i in range(len(self.adjMat[idx])):
      if (self.adjMat[idx][i] != 0):
        nList.append(self.Vertices[i])
    return nList

  # get a copy of the list of vertices
  def getVertices (self):
    return self.Vertices[:]
  
  # Helper method for hasCycle, determines whether vertex at index u
  # links to vertex at index i (in the self.Vertices list)
  def linksTo(self, u, v):
    for edge in self.Edges:
      if (edge.u == self.Vertices[u]) and (edge.v == self.Vertices[v]):
        return True
    return False
  
  # determine if the graph has a cyclex
  def hasCycle (self):
    # Modified dfs for each vertex
    for i in range(len(self.Vertices)):
      # create a stack
      theStack = Stack()
      
      # mark the vertex as visited and push on the stack
      (self.Vertices[i]).visited = True
      theStack.push (i)
      
      # Once empty, all vertices have been visited
      while (not theStack.isEmpty()):
        # Actual modification: detects if there is a back edge to the 
        # starting vertex
        if self.linksTo(theStack.peek(), i):
          return True
        # get an adjacent unvisited vertex
        u = self.getAdjUnvisitedVertex (theStack.peek())
        if (u == -1):
          u = theStack.pop() 
        else:
          (self.Vertices[u]).visited = True
          theStack.push(u)
      
      # stack is empty reset the flags
      self.resetVisited()

    return False

  # Helper for toposort
  def topoDFS(self, v, stack):
    self.Vertices[v].visited = True
    neighbors = self.getNeighbors(self.Vertices[v].label)
    for vertex in neighbors:
      if (vertex.visited == False):
        self.topoDFS(self.getIndex(vertex.label), stack)
    stack.push(v)
    
  # return a list of vertices after a topological sort
  def toposort (self):
    if (not self.hasCycle()): 
      theStack = Stack()
      for vertex in self.Vertices:
        if (vertex.visited == False):
          self.topoDFS(self.getIndex(vertex.label), theStack)
      
      # reset the flags for every vertex
      self.resetVisited()
      return theStack
    return None

  # prints a list of edges in ascending order of their weights
  # list is in the form [v1 - v2, v2 - v3, ..., vm - vn]
  def edgeList (self):
    # Helper selection sort function
    def selectionSort(a):
      for i in range(len(a) - 1):
        min = a[i]
        minIdx = i
        for j in range(i + 1, len(a)):
          if (a[j] < min):
            min = a[j]
            minIdx = j
        a[minIdx] = a[i]
        a[i] = min
    
    edgesCopy = self.Edges[:]
    selectionSort(edgesCopy)
    for edge in edgesCopy:
      print (str(edge.u) + '--' + str(edge.v) + ' ' + str(edge.weight))

  # determine shortest path from a single vertex
  def shortestPath (self, fromVertexLabel):
    startIdx = self.getIndex(fromVertexLabel)
    INF = '~' # Representation of infinity
    distances = [] # List that will store distances as the algorithm is processed
    # Initializing the list
    for i in range(len(self.Vertices)):
      if (i == startIdx):
        distances.append(0)
      else:
        distances.append(INF)
    
    # Mark starting vertex as visited, and create set of all unvisited
    # vertices
    (self.Vertices[startIdx]).visited = True
    unvisitedSet = list()
    for vertex in self.Vertices:
      #if (vertex.visited == False):
      unvisitedSet.append(vertex)
        
    # Initializing current as vertex at index startIdx and getting neighbors
    current = self.Vertices[startIdx]
    neighbors = self.getNeighbors(current.label)
    # While there are still neighbors of the current vertex
    while (len(unvisitedSet) > 0):#(len(neighbors) > 0):
      for v in neighbors:
        if (not v.wasVisited()):
          # if v connects to starting vertex through
          dist = (self.getEdgeWeight(current.label, v.label) + distances[self.getIndex(current.label)])
          
          # Compares current distance value with one in distances list
          vIdx = self.getIndex(v.label)
          if (distances[vIdx] == INF) or (distances[vIdx] > dist):
            distances[vIdx] = dist
      
      current.visited = True
      if current in unvisitedSet:
        unvisitedSet.remove(current)
      
      # Select closest unvisited vertex to be current
      minDist = 1000000 # Using arbitrarily large number cause I can't think any more logically than that.
      for v in unvisitedSet:
        if v in neighbors:
          idx = self.getIndex(v.label)
          if (distances[idx] == INF):
            minDist = INF
            minIdx = idx
            break
          elif (distances[idx] < minDist):
            minDist = distances[idx]
            minIdx = idx
      # Resetting current and getting neighbors of current
      current = self.Vertices[minIdx]
      neighbors = self.getNeighbors(current.label)

    # reset the flags for every vertex
    self.resetVisited()
    
    return distances

  # delete an edge from the adjacency matrix
  def deleteEdge (self, fromVertexLabel, toVertexLabel):
    # Remove from list of edges
    for edge in self.Edges:
      if (edge.u.label == fromVertexLabel) and (edge.v.label == toVertexLabel):
        self.Edges.remove(edge)
    # Change value in adjacency matrix to 0
    i = self.getIndex(fromVertexLabel)
    j = self.getIndex(toVertexLabel)
    self.adjMat[i][j] = 0

  # delete a vertex from the vertex list and all edges from and
  # to it in the adjacency matrix
  def deleteVertex (self, vertexLabel):
    # Remove the row and column that corresponded to that vertex
    idx = self.getIndex(vertexLabel)
    nVert = len(self.Vertices)
    for i in range(nVert):
      self.adjMat[i].remove(self.adjMat[i][idx])
    self.adjMat.remove(self.adjMat[idx])
    
    # Deleting all edges associated with the vertex from list of edges
    copy = self.Edges[:]
    self.Edges = []
    for edge in copy:
      if (edge.u.label != vertexLabel) and (edge.v.label != vertexLabel):
        self.Edges.append(edge)
        
    # Deleting the vertex for list of vertices
    del self.Vertices[idx]
    
def main():

  # Create Graph object
  cities = Graph()

  # Open file for reading
  inFile = open ("./graph.txt", "r")

  # Read the vertices
  numVertices = int ((inFile.readline()).strip())
  #print (numVertices)

  for i in range (numVertices):
    city = (inFile.readline()).strip()
    #print (city)
    cities.addVertex (city)

  # Read the edges
  numEdges = int ((inFile.readline()).strip())
  #print (numEdges)

  for i in range (numEdges):
    edge = (inFile.readline()).strip()
    #print (edge)
    edge = edge.split()
    start = int (edge[0])
    finish = int (edge[1])
    weight = int (edge[2])
    cities.addDirectedEdge (start, finish, weight)

  # Read the starting vertex for dfs, bfs, and shortest path
  startVertex = (inFile.readline()).strip()
  #print (startVertex)
  
  # Get the index of startVertex
  startIndex = cities.getIndex(startVertex)

  # Close file
  inFile.close()

  # test depth first search
  print ("DFS from " + startVertex + ':')
  cities.dfs (startIndex)
  print()

  # test breadth first search
  print ("BFS from " + startVertex + ':')
  cities.bfs (startIndex)
  print()

  # test topological sort
  print ('Topological Sort:')
  stack = cities.toposort()
  if (stack == None):
    print ('Error: Graph has cycle.')
  else:
    for i in range(stack.size()):
      print (cities.Vertices[stack.pop()])
  print()

  # test edge list in ascending order of weights
  print ('Ascending Edges:')
  cities.edgeList()
  print()

  # test single source shortest path algorithm
  print ('SSSP from ' + startVertex + ' (~ = infinity):')
  results = cities.shortestPath(startVertex)
  for i in range(len(results)):
    if (i != cities.getIndex(startVertex)):
      print (startVertex + '->' + str(cities.Vertices[i]) + ': ' + str(results[i]))
  print()

main()