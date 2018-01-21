## Zero Nevative Values ##
#######   Python   #######

def zeroNegativeValues(arr):
	for i in range(len(arr)):
		if arr[i] < 0:
			arr[i]=0
	print arr

arr = [7, 3, 28, -8, 0, -2, -1, 69, 64, -8]

zeroNegativeValues(arr)