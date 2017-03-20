#  File: BabyNames.py 

#  Description: This program provides an interactive interface for the user. It gives the user options to get info on baby name data (which is read in and stored in a dictionary), and loops the options until the user either chooses 7 or gives invalid input.

#  Student Name: Blake Kappel

#  Student UT EID: bak792

#  Course Name: CS 313E

#  Unique Number: 51730

#  Date Created: 3/10/2015

#  Date Last Modified: 3/20/2017

######################################################################

# Return True if items in list are getting smaller, False if not
def gettingSmaller(a):
  for i in range(len(a)):
    if a[i] == 0:
      a[i] = 1001
  for i in range(1, len(a)):
    if (a[i] >= a[i - 1]):
      return False
  return True

# Return True if items in list are getting larger, False otherwise
def gettingLarger(a):
  for i in range (len(a)):
    if a[i] == 0:
      a[i] = 1001
  for i in range(1, len(a)):
    if (a[i] <= a[i -1]):
      return False
  return True
  
# Returns True if name is a key in the dictionary, False if not
def nameInDict(name, dict):
  return name in dict
  
# Returns all the rankings for a given name
def giveRankings(name, dict):
  return dict[name]

# Returns a list of names that have a rank in all the decades in sorted order by name
def rankInAll(dict):
  list = []
  for key in dict:
    if 0 not in dict[key]:
      list.append(key)
  list.sort()
  return list

# Returns a list of sorted names that only appear in one decade
def rankInOne(dict, dec):
  list = []
  dec = dec % 1900 // 10
  for key in dict:
    count = 0
    for rank in dict[key]:
      if (rank == 0):
        count += 1
    if (count == 10) and (dict[key][dec] != 0):
      list.append(key)
  list.sort()
  return list
  
  
# Returns list of names in alphabetical order that have a rank in a given decade
def allHasRank(dict, decade):
  list = []
  decade = (decade % 1900) // 10
  for name in dict:
    if (dict[name][decade] != 0):
      list.append(name)
  list.sort()
  return list
  
# Return list of all names in alphabetical order that are increasing in popularity in all decades
def gettingPopular(dict):
  list = []
  for name in dict:
    # Append name to list if rankings decrease every decade
    if gettingSmaller(dict[name]):
      list.append(name)
    # Change 1001s back to 0s
    for i in range(len(dict[name])):
      if (dict[name][i] == 1001):
        dict[name][i] = 0
  list.sort()
  return list
  
# Return list of all names that are getting less popular in every decade
def gettingLame(dict):
  list = []
  for name in dict:
    # Append name to list if rankings increase every decade
    if gettingLarger(dict[name]):
      list.append(name)
    # Change 1001s back to 0s
    for i in range(len(dict[name])):
      if (dict[name][i] == 1001):
        dict[name][i] = 0
  list.sort()
  return list

# Returns the decade of the highest rank for a given name
def highestRankDecade(name, dict):
  hi = 1000
  for rank in dict[name]:
    if (rank < hi) and (rank != 0):
      hi = rank
      idx = dict[name].index(rank)
  return 1900 + (idx * 10)
      
  
def main():
  # Open this bad boy
  namesFile = open('names.txt', 'r')
  
  # Initialize master Dictionary
  namesDict = {}
  
  # Fills dictionary with data from names.txt; name is key, list of rankings for each decade is value
  for line in namesFile:
    name, d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10 = line.split(' ')
    rankings = [d0, d1, d2, d3, d4, d5, d6, d7, d8, d9, d10]
    for i in range(len(rankings)):
      rankings[i] = int(rankings[i])
    namesDict[name] = rankings
  
  # Close this bad boy
  namesFile.close()

  # Interactive program interface
  while True:
    # Option explanations
    print ('Options:')
    print ('Enter 1 to search for names.')
    print ('Enter 2 to display data for one name.')
    print ('Enter 3 to display all names that appear in only one decade.')
    print ('Enter 4 to display all names that appear in all decades.')
    print ('Enter 5 to display all names that are more popular in every decade.')
    print ('Enter 6 to display all names that are less popular in every decade.')
    print ('Enter 7 to quit. \n')
    
    # Option 1
    choice = int(input('Enter choice: '))
    if choice == 1:
      name = input('Enter a name: ')
      # Output for case where name is not ranked in any decade (not in dictionary)
      if nameInDict(name, namesDict):
        print ('\nThe matches with their highest ranking decade are:')
        print (name, str(highestRankDecade(name, namesDict)))
      # If name is in dictionary (ranked in some decade), displays the name and its highest ranking decade
      else:
        print (name, 'does not appear in any decade.')
      print()
    
    # Option 2
    elif choice == 2:
      name = input('Enter a name: ')
      if nameInDict(name, namesDict):
        ranks = giveRankings(name, namesDict)
        # First line of output
        print (name + ': ' + ' '.join(str(i) for i in ranks))
        # Lines for individual decades
        idx = 0
        for i in range(1900, 2010, 10):
          print (str(i) + ': ' + str(ranks[idx]))
          idx += 1
      else:
        print (name, 'does not appear in any decade.')
      print()
      
    # Option 3      
    elif choice == 3:
      decade = int(input('Enter decade: '))
      print ('The names are in alphabetical:')
      namesList = rankInOne(namesDict, decade)
      for name in namesList:
        print (name)
      print()
        
    # Option 4
    elif choice == 4:
      namesList = rankInAll(namesDict)
      print (len(namesList), 'names appear in every decade. The names are:')
      for name in namesList:
        print (name)
      print()
    
    # Option 5
    elif choice == 5:
      namesList = gettingPopular(namesDict)
      print (str(len(namesList)) + ' names are more popular in every decade.')
      for name in namesList:
        print (name)
      print()

    # Option 6
    elif choice == 6:
      namesList = gettingLame(namesDict)
      print (str(len(namesList)) + ' names are less popular in every decade.')
      for name in namesList:
        print (name)
      print()
    
    # Option 7
    elif choice == 7:
      print ('\n\nGoodbye.')
      return
      
main()
