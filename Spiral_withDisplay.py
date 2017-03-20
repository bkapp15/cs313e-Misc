# File: Spiral.py

# Description:

# Student Name: Blake Kappel

# Student UT EID: bak792

# Partner Name: Jacob Martinez

# Partner UT EID: jam22426

# Course Name: CS 313E

# Unique Number: 51730

# Date Created: 1/27/2015

# Date Last Modified: 1/27/2015

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

	#check
	print ('Dimension =', dim)
	print ('Target number =', targetNum, '\n')
	
	# Error if target number is not within the range
	if (targetNum < 1) or (targetNum > dim**2):
		print ("Number not in Range.")
		return
		
	# Error if target number will be on outer edge of spiral
	if (targetNum > dim**2 - (dim*4 - 4)): #and (targetNum != 1):
		print ("Number on Outer Edge.")
		return
		
	#Initialize 2d spiral according to dimension and fill with 0's
	spiral = []
	for i in range (0, dim):
		new = []
		for j in range (0, dim):
			new.append(0)
		spiral.append(new)
		
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
	
	print ('Initial =', x, y)
	
	# Function that will store x and y coordinates of the targetNum in 
	# the grid to targetX and targetY
	def targetCheck(num, x, y):
		if num == targetNum:
			global targetX
			global targetY
			targetX = x
			targetY = y
	# Counts the layers of squares to be printed
	squareCount = 1
	
	# Sequentially assigns every number to specified 2-d list locations
	while (nextNum > 0):
		
		print ("\nSquare layer:", squareCount)
		
		# Assign numbers to top row of square layer; constant y-value
		while (x > indMin):
			x -= 1
			spiral[y][x] = nextNum
			targetCheck(nextNum, x, y)
			nextNum -= 1
		print ('First =',x, y)
		
		# Assign numbers to left column of square layer; constant x-value
		while (y < -indMin - 1):
			y += 1
			spiral[y][x] = nextNum
			targetCheck(nextNum, x, y)
			nextNum -= 1
		print ('Second =', x, y)
		
		# Assign numbers to bottom row of square layer; constant y-value
		while (x < indMax):
			x += 1
			spiral[y][x] = nextNum
			targetCheck(nextNum, x, y)
			nextNum -= 1
		print ('Third =', x, y)
		
		# Assign numbers to right column of square layer; constant x-value
		while (y > -indMax):
			y -= 1
			spiral[y][x] = nextNum
			targetCheck(nextNum, x, y)
			nextNum -= 1
		print ('Fourth =', x, y)
		
		# Moves into next square layer
		indMax -= 1
		indMin += 1
		
		squareCount += 1
	
	# Display the coordinates of the target number
	print('\nTarget x-value =', targetX)
	print('Target y-value =', targetY, '\n')

	# Print the visual grid
	for a in spiral:
		for b in a:
			print (b, end = ' ')
		print ('\n')
	
	# Assign upper, lower, right, and left x and y vals
	UY = targetY - 1
	LY = targetY + 1
	RX = targetX + 1
	LX = targetX - 1
	
	print (spiral[UY][LX], spiral[UY][targetX], spiral[UY][RX])
	print (spiral[targetY][LX], targetNum, spiral[targetY][RX])
	print (spiral[LY][LX], spiral[LY][targetX], spiral[LY][RX])
	
main()
