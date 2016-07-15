def isLengthGrater(string, size):
	for word in string.strip().split('+'):
		if len(word) > size:
			return True
	return False

ten = open('astadhayi.txt.out.10','w')
twe = open('astadhayi.txt.out.20','w')
thi = open('astadhayi.txt.out.30','w')
fort = open('astadhayi.txt.out.40','w')
fif = open('astadhayi.txt.out.50','w')

san = open('astadhayi.txt.out.san.merge','w')
int = open('astadhayi.txt.out.int.inria.merge','w')
ext = open('astadhayi.txt.out.ext.inria.merge','w')

sanMap = {}
for line in open('astadhayi.txt.san.merge').readlines():
	line = line.strip().split(',')
	if line[-1] == '1' or line[-1] == 1:
		sanMap[line[0]] = 1
		
extinria = {}
for line in open('astadhayi.txt.ext.inria').readlines():
	line = line.strip().split(':')
	if line[-1] == '1' or line[-1] == 1:
		extinria[line[0]] = 1
		
intinria = {}
for line in open('astadhayi.txt.int.inria').readlines():
	line = line.strip().split(':')
	if line[-1] == '1' or line[-1] == 1:
		intinria[line[0]] = 1

	

for line in open('astadhayi.txt.out').readlines():
	line = line.strip().replace('"','')
	lineSplit = line.split(',');
	if not isLengthGrater(lineSplit[2], 10):
		ten.write(line+'\n');
	if not isLengthGrater(lineSplit[2], 20):
		twe.write(line+'\n');
	if not isLengthGrater(lineSplit[2], 30):
		thi.write(line+'\n');
	if not isLengthGrater(lineSplit[2], 40):
		fort.write(line+'\n');
	if not isLengthGrater(lineSplit[2], 50):
		fif.write(line+'\n');

	if sanMap.has_key(lineSplit[0]):
		san.write(line+'\n')

	if extinria.has_key(lineSplit[0].split(':')[0]):
		ext.write(line+'\n')
	if intinria.has_key(lineSplit[0].split(':')[0]):
		int.write(line+'\n')
	
ten.close()
twe.close()
thi.close()
fort.close()
fif.close()