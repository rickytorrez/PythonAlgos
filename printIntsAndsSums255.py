## Print Ints & Sum to255 Odds##
###########   Python   #########

def printIntsAndsSums255():
	sum = 0
	for i in range(1,256):
		sum += i
		print i, sum

printIntsAndsSums255()