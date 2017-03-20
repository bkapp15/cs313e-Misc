# File: stackBalanceBrackets.py

# Author: Blake Kappel

# Description: Simple exercise using the Stack object and methods to test whether a math expression's brackets are balanced or not.

# Date last modified: 3/20/2017

##############################################################################################

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

def bracketsBalance(exp):
  """exp is a string that represents the expression"""
  stk = Stack() # Create a new stack
  for ch in exp: # Scan across the expression
    if ch in ['[', '(']: # Push an opening bracket
      stk.push(ch)
    elif ch in [']', ')']: # Process a closing bracket
      if stk.isEmpty(): # Not balanced
        return False
      chFromStack = stk.pop()
      # Brackets must be of same type and match up
      if (ch == ']' and chFromStack != '[') or (ch == ')' and chFromStack != '('):
          return False
  return stk.isEmpty()



def main():
  exp = input("Enter a bracketed expression: ")
  if bracketsBalance(exp):
    print("OK")
  else:
    print("Not OK")


main()
