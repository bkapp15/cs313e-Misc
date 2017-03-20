# File: Spiral.py

# Description: This program outputs a specific target number and it's neighbouring numbers from a square spiral. It first creates a virtual spiral by initializing a 2d list, then inserting numbers of decreasing value using series of loops, starting with the highest number at the top right corner and ending with 1 in the center. The coordinates of the target number are stored during the spiral creation. They are then used to determine the target's neighbouring numbers, which are then outputted in the format that they would appear in the spiral.

# Student Name: Blake Kappel

# Student UT EID: bak792

# Partner Name: Jacob Martinez

# Partner UT EID: jam22426

# Course Name: CS 313E

# Unique Number: 51730

# Date Created: 1/27/2015

# Date Last Modified: 1/31/2015

####################################################################################

def main():

	# Open spiral.txt file, read in contents and assign dimension (dim) and targetNum variables
	openFile = open("spiral.txt", 'r')
	dim = openFile.readline()
	dim = dim.rstrip('\n')
	dim = int(dim)
	targetNum = int(openFile.readline())
	openFile.close()
	
	# If dimension is not odd, add 1 to make it odd
	if (dim % 2 == 0):
		dim += 1
	
	# Error if target number is not within the range
	if (targetNum < 1) or (targetNum > dim**2):
		print ("Number not in Range.")
		return
		
	# Error if target number will be on outer edge of spiral
	if (targetNum > dim**2 - (dim*4 - 4)) or (dim == 1):
		print ("Number on Outer Edge.")
		return
		
	#Initialize 2d spiral according to dimension and fill with 0's
	spiral = []
	for i in range (0, dim):
		new = []
		for j in range (0, dim):
			new.append(0)
		spiral.append(new)

	#Initialize the number variable that will be inserted into position
	nextNum = dim**2
	
	# Minimum and maximum index values to be adjusted as the loop goes
	# through the spiral layers
	indMin = 0
	indMax = dim - 1
	
	# Initialize the x and y coordinates; y is negative to account for 
	# the structural deviation between the indices in the 2d list and the 
	# printed visual grid
	x = dim
	y = -dim
	
	# Function that will store x and y coordinates of the targetNum in 
	# the grid to targetX and targetY
	def targetCheck(num, x, y):
		if num == targetNum:
			global targetX
			global targetY
			targetX = x
			targetY = y
	
	# Sequentially assigns every number to specified 2d list locations
	while (nextNum > 0):

		# Assign numbers to top row of square layer; manipulates x-value; 
		# constant y-value
		while (x > indMin):
			x -= 1
			spiral[y][x] = nextNum
			targetCheck(nextNum, x, y)
			nextNum -= 1
		
		# Assign numbers to left column of square layer; manipulates y-value;
		# constant x-value
		while (y < -indMin - 1):
			y += 1
			spiral[y][x] = nextNum
			targetCheck(nextNum, x, y)
			nextNum -= 1
		
		# Assign numbers to bottom row of square layer; manipulates x-value;
		# constant y-value
		while (x < indMax):
			x += 1
			spiral[y][x] = nextNum
			targetCheck(nextNum, x, y)
			nextNum -= 1
		
		# Assign numbers to right column of square layer; manipulates 
		# y-value; constant x-value
		while (y > -indMax):
			y -= 1
			spiral[y][x] = nextNum
			targetCheck(nextNum, x, y)
			nextNum -= 1
		
		# Moves into next square layer
		indMax -= 1
		indMin += 1

	# Assign upper, lower, right, and left x and y vals to be used in final
	# output
	UY = targetY - 1
	LY = targetY + 1
	RX = targetX + 1
	LX = targetX - 1
	
	# Final output
	print (spiral[UY][LX], spiral[UY][targetX], spiral[UY][RX])
	print (spiral[targetY][LX], targetNum, spiral[targetY][RX])
	print (spiral[LY][LX], spiral[LY][targetX], spiral[LY][RX])
	
main()
