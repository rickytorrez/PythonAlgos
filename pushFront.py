## Push Front ##
### Python #####

def pushFront(arr, val):
	arr.append(0)
	for i in range(len(arr)-1,0,-1):
		arr[i] = arr[i-1]
	arr[0] = val
	print arr

arr = [7, 3, 28, -8, 0, -2, -1, 69, 64, -8]
string = "Hola"

pushFront(arr, 7)