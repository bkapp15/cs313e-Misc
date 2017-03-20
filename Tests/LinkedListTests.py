#TestLinkedList is the file name where the class is created (TestLinkedList.py)
import TestLinkedList as LL 

grade = 0
# 10 points for the Header
grade +=10 #assuming you did it properly

# 10 points #############Create linked lists here#################
try:
  list1 = LL.LinkedList()
  list1.addFirst(8)
  list1.addFirst(7)
  list1.addFirst(5)
  list1.addFirst(2)
  list1.addFirst(4)
  list2 = LL.LinkedList()
  list2.addFirst(10)
  list2.addFirst(3)
  list2.addFirst(6)
  list2.addFirst(1)
  list2.addFirst(9)
  list3 = LL.LinkedList()
  list4 = LL.LinkedList()
  grade+=10
  print ('Pass: Create linked lists') # Me
except:
  print("Something broke in Create linked lists")
#Check your functions here, 
#if assertion fails, error is shown on console

# 35 points ##########Test Construction################
try:
  assert list1.isEmpty() == False
  assert list2.isEmpty() == False
  assert list1.isEqual(list2) == False
  assert list3.isEmpty() == True
  print("Pass: isEmpty") # Me
  assert list2.getNumLinks()==list1.getNumLinks()
  list3.addFirst(1)
  list3.addFirst(2)
  list3.addLast(3)
  assert list3.__str__() == "2  1  3"
  print('Pass: string')
  list4.addInOrder(1)
  list4.addInOrder(3)
  list4.addInOrder(5)
  list4.addInOrder(2)
  list4.addInOrder(4)
  assert list4.__str__() == "1  2  3  4  5"
  assert list2.copyList().isEqual(list2)
  assert list4.reverseList().__str__() == "5  4  3  2  1"
  assert list3.delete(4) == None
  list3.delete(2)
  assert list3.__str__() == "1  3"
  grade +=35
except:
  print("Something broke in Test Construction")

# 15 points###########Test searching####################
try:
  assert list4.findOrdered(3) != None
  assert list4.findOrdered(6) == None
  assert list2.findUnordered(4) == None
  assert list2.findUnordered(1) != None
  grade += 15
except:
  print("Something broke in Test Searching")

# 20 points###########Test Sorting#######################
try:
  assert list2.isSorted() == False
  assert list2.sortList().isSorted() == True
  grade+=20
except:
  print("Something broke in Test Sorting")


# 10 points###########Test Other functions################
try:
  list2 = list2.sortList()
  assert list2.mergeList(list1.sortList()).__str__() == "1  2  3  4  5  6  7  8  9  10"
  list4.addFirst(5)
  list4.addFirst(2)
  assert list4.sortList().removeDuplicates().__str__() == "1  2  3  4  5"
  grade+=10
except:
  print("Something broke in Test Other functions")