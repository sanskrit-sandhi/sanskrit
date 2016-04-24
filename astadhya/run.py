'''file2 = open('out.txt').readlines()
file1 = open('padacCheda.txt').readlines()
out = open("sandhis.csv",'w')
for i in range(len(file1)):
	out.write('"'+file1[i].split('\t')[0].strip()+'","'+file2[i].strip()+'",\n')
out.close()'''

'''file1 = open('astadhya.txt').readlines()
file2 = open('sandhis.csv').readlines()
out = open("sandhis_no.csv",'w')
for i in range(len(file1)):
	out.write('"'+file1[i].split('\t')[0].strip()+'","'+file1[i].split('\t')[1].strip()+'","'+file1[i].split('\t')[2].strip()+'",'+file2[i].strip()+'\n')
out.close()'''


def isLengthGrater(string):
	return False
	if len(string.strip().split(' ')) > 2:
		return True
	for word in string.strip().split(' '):
		if len(word) > 25:
			return True
	return False

eq = open('eq_sandhis_nowordlength.csv','w')
neq = open('neq_sandhis_nowordlength.csv','w')
for line in open('sandhis.csv').readlines():
	line = line.strip().replace('"','')
	line = line.split(',');
	if len(line) != 6:
		print line
	elif line[3].strip().replace(' ','') == line[4].strip().replace(' ','') or len(line[4].split(' ')) == 1 or '-' in line[4] or isLengthGrater(line[4]):
		eq.write('"'+line[0].strip()+'","'+line[1].strip()+'","'+line[2].strip()+'","'+line[3].strip()+'","'+line[4].strip().replace(' ','+')+'",\n')
	elif line[3].strip().replace(' ','') != line[4].strip().replace(' ',''):
		neq.write('"'+line[0].strip()+'","'+line[1].strip()+'","'+line[2].strip()+'","'+line[3].strip()+'","'+line[4].strip().replace(' ','+')+'",\n')
eq.close()
neq.close()
		
		
	