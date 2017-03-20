#  File: BST_Cipher.py

#  Description: This program modifies the binary search tree class to be able to encrypt and decrypt strings. It then tests these methods on strings given through an input file and prints to console the results of the tests.

#  Student Name: Blake Kappel

#  Student UT EID: bak792

#  Partner Name: Jacob Martinez

#  Partner UT EID: jam22426

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 4/22/2015

#  Date Last Modified: 4/24/2015

############################################################

class Node (object):
  # Constructor
  def __init__(self, data):
    self.data = data
    self.lChild = None
    self.rChild = None
   
  # String representation  
  def __str__(self):
    return str(self.data)

class Tree (object):
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
    
    
def main():

  f = open('cipherInput.txt')
  s=0
  while(s<8):
    key = f.readline().strip()
    encode = f.readline().strip()
    decode = f.readline().strip()
    skip = f.readline()
    s+=1
    t = Tree(key)
    print(t.encrypt(encode))
    print(t.decrypt(decode))
    print()
    
  f.close()
  
main()
