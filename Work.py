#  File: Work.py 

#  Description: This program solves the assignment dilemma for Vyasa. It reads in test cases and solves what the minimum of value of v can be and he still finishes the assignment before falling asleep. This is done using a find_v function (modified version of binary search) which calls on a check function that runs a test to see if the mid value can be a potential solution. The output for each test case is the solution for v.

#  Student Name: Blake Kappel

#  Student UT EID: bak792

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 3/25/2015

#  Date Last Modified: 3/26/2015

###########################################################

# Checks to see if num can work with n and k; returns True if it checks, False if it doesn't
def check(n, k, num):
  # Initialize p and sum of the series, where p is number of the cup of coffee
  p, sum = 1, num
  # Runs the series essentially until num either passes or fails
  while (sum < n) and (num//k**p != 0):
    sum += num//k**p
    p += 1
  return (sum >= n)
  
# The function that calculates minimum possible value for v
def find_v (n, k):
  lo, hi = 1, n
  while (lo <= hi):
    mid = (lo + hi)//2
    # Need to raise lo if mid does not check out, because the solution must be larger
    if not check(n, k, mid):
      lo = mid + 1
    # Lowers hi and stores mid as potential v if it passes, because the solution for v could still be smaller
    elif check(n, k, mid):
      hi = mid - 1
      v = mid
  return v

def main():
  
  # Open work.txt file, read in data
  workFile = open('work.txt', 'r')
  # t is number of test cases
  t = workFile.readline()
  t = int(t)
  
  # For every test case, run the code that calculates v
  for i in range(t):
    # From each line (test case), obtain the int values for n and k
    line = workFile.readline()
    n, k = line.split(' ')
    n, k = int(n), int(k)
    
    # Output the solutions
    print (find_v(n, k))    
  
  workFile.close()
  
main()