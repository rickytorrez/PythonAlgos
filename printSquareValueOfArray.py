## Print Square Value ##
######   Python   ######

def squareValues(arr):
	for i in range(0,len(arr)): 
		arr[i] = arr[i]**2
	print arr

arr = [7, 3, 28, -8, 0, -2, -1, 69, 64, -8]

squareValues(arr)