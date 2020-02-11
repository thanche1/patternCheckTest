import re

def checkMe(x):
	checkFile = open(x, "r")
	regex = re.compile('jjj*')

	for line in checkFile:
		check_my_pattern = regex.findall(line)
		for word in check_my_pattern:
			print (word)

	