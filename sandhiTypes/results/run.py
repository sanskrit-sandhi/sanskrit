
import sys, os

paths = ['astadhyayi', 'gita', 'gold', 'literature', 'uoh']

vis = open('visarga','w')
con = open('consonant','w')
vow = open('vowel','w')

vism = open('visargamerge','w')
conm = open('consonantmerge','w')
vowm = open('vowelmerge','w')

def updateMap(line, map):
	if line[2] == '1' or line[2] == 1:
		map['jnu'] = map['jnu'] + 1;
	if line[3] == '1' or line[3] == 1:
		map['inria'] = map['inria'] + 1;
	if line[5] == '1' or line[5] == 1:
		map['uoh'] = map['uoh'] + 1;

	if line[7] == '1' or line[7] == 1:
		map['jnum'] = map['jnum'] + 1;
	if line[10] == '1' or line[10] == 1:
		map['inriam'] = map['inriam'] + 1;
	if line[9] == '1' or line[9] == 1:
		map['uohm'] = map['uohm'] + 1;

	return map

def getPercent(num, denom):
	return str(format(float(num*100)/denom, '.2f'))

def writeToFile(path, out, outm, map, count):
	out.write(str(paths.index(path))+'\t'+path+'\t'+getPercent(map['jnu'],count)+'\t'+getPercent(map['uoh'],count)+'\t'+getPercent(map['inria'],count)+'\n')
	outm.write(str(paths.index(path))+'\t'+path+'\t'+getPercent(map['jnu'],count)+'\t'+getPercent(map['uohm'],count)+'\t'+getPercent(map['inriam'],count)+'\n')


def processFile(path):
	visarga = {'jnu':0, 'uoh':0, 'inria':0, 'jnum':0, 'uohm':0, 'inriam':0}
	consonant = {'jnu':0, 'uoh':0, 'inria':0, 'jnum':0, 'uohm':0, 'inriam':0}
	vowel = {'jnu':0, 'uoh':0, 'inria':0, 'jnum':0, 'uohm':0, 'inriam':0}
	count = {'vis':0, 'vow':0, 'cons':0}

	for line in open(path).readlines():
		line = line.strip().split('\t')
		if line[1] == 'visarga':
			visarga =updateMap(line,visarga)
			count['vis'] = count['vis']+1

		elif line[1] == 'consonant':
			consonant=updateMap(line,consonant)
			count['cons'] = count['cons']+1
		
		elif line[1] == 'vowel':
			vowel=updateMap(line,vowel)
			count['vow'] = count['vow']+1
	print path
	writeToFile(path, vis, vism, visarga, count['vis'])
	writeToFile(path, con,conm, consonant,count['cons'])
	writeToFile(path, vow,vowm, vowel, count['vow'])

def main():
	#path = sys.argv[1]
	for path in paths:
		processFile(path)
	vis.close()
	con.close()
	vow.close()

if __name__ =="__main__":
	main()