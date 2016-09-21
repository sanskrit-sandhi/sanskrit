def isLengthGrater(string, size):
	for word in string.strip().split('+'):
		if len(word) > size:
			return True
	return False

out = open('astadhayi.txt.size','w')


for line in open('astadhayi.txt.out').readlines():
	line = line.strip().replace('"','')
	lineSplit = line.split(',');
	if isLengthGrater(lineSplit[2], 40):
		out.write(lineSplit[0]+',50'+'\n');
	elif isLengthGrater(lineSplit[2], 30):
		out.write(lineSplit[0]+',40'+'\n');
	elif isLengthGrater(lineSplit[2], 20):
		out.write(lineSplit[0]+',30'+'\n');
	elif isLengthGrater(lineSplit[2], 10):
		out.write(lineSplit[0]+',20'+'\n');
	elif isLengthGrater(lineSplit[2], 0):
		out.write(lineSplit[0]+',10'+'\n');
	else:
		out.write(lineSplit[0]+',0'+'\n');

	
	
out.close()