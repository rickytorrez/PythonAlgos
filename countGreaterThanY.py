## Print Count Greater Than Y ##
##########   Python   ##########

def countGreaterThanY(arr, y):
	count = 0
	for i in range(len(arr)):
		if arr[i] > y:
			count +=1
	print count


arr = [7, 3, 28, -8, 0, -2, -1, 69, 64, -8]

countGreaterThanY(arr, 16)