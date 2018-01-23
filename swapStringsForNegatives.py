## Swap String for Negatives ##
#########   Python   ##########

def swapStringForNegatives(arr, string):
	for i in range(len(arr)):
		if arr[i]< 0:
			arr[i]=string
	print arr

arr = [7, 3, 28, -8, 0, -2, -1, 69, 64, -8]
string = "Coding Dojo"

swapStringForNegatives(arr, string)