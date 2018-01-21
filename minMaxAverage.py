## minMax Average ##
####   Python   ####

def minMaxAverage(arr):
	min = arr[0] 
	max = arr[0]
	sum = 0
	for i in range(len(arr)):
		sum+=arr[i]
		if arr[i]>max:
			max=arr[i]
		if arr[i]<min:
			min=arr[i]
	print min, max, sum/float(len(arr))

arr = [7, 3, 28, -8, 0, -2, -1, 69, 64, -8]

minMaxAverage(arr)