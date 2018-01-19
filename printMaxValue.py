## Print Max Value in the Array Odds##
#############   Python   #############

def printMax(arr):
	max = arr[0]
	for val in arr:
		if val > max:
			max = val
	print max

arr = [7, 3, 28, -8, 0, -2, -1, 69, 64, -8]

printMax(arr)