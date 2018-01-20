## Print Average Value in the Array Odds##
###############   Python   ###############

def printAverage(arr):
	sum = arr[0]
	for var in range(1, len(arr)):
		sum += arr[var]
	print sum / float(len(arr))

arr = [7, 3, 28, -8, 0, -2, -1, 69, 64, -8]

printAverage(arr)