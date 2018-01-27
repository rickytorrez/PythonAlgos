## Character Count ##
###### Python #######

def characterCount(sentence):
	count = 0
	for i in range (0,len(sentence)):
		if not sentence[i].isspace():
			count += 1
	print count

sentence = " Lorem ipsum   dolor sit  amet! "

characterCount(sentence)