# File: QueueTesting.py

############################33

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

    
def main():
  
  Q1 = Queue()
  Q1.enqueue(2)
  print (Q1.dequeue())
  try:
    print(Q1.dequeue())
  except:
    print ('Error')
    
  Q1.enqueue(3)
  Q1.enqueue(10)
  print (Q1.size())
  print (Q1.isEmpty())
  print(Q1.dequeue())
  print (Q1.dequeue())
  
main()