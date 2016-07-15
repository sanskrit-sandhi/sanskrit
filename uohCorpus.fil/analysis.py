import sys

file = sys.argv[1]

def isLengthGrater(string, size):
	for word in string.strip().split('+'):
		if len(word) > size:
			return True
	return False

san = open(file+'.out.san.merge','w')
int = open(file+'.out.int.inria.merge','w')
ext = open(file+'.out.ext.inria.merge','w')

sanMap = {}
for line in open(file+'.san.merge').readlines():
	line = line.strip().split(',')
	if line[-1] == '1' or line[-1] == 1:
		sanMap[line[0]] = 1
		
extinria = {}
for line in open(file+'.ext.inria').readlines():
	line = line.strip().split(':')
	if line[-1] == '1' or line[-1] == 1:
		extinria[line[0]] = 1
		
intinria = {}
for line in open(file+'.int.inria').readlines():
	line = line.strip().split(':')
	if line[-1] == '1' or line[-1] == 1:
		intinria[line[0]] = 1

	

for line in open(file+'.out').readlines():
	line = line.strip().replace('"','')
	lineSplit = line.split(',');
	
	if sanMap.has_key(lineSplit[0]):
		san.write(line+'\n')

	if extinria.has_key(lineSplit[0]):
		ext.write(line+'\n')
	if intinria.has_key(lineSplit[0]):
		int.write(line+'\n')
	
san.close()
ext.close()
int.close()

