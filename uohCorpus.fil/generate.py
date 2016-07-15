from os import listdir
import sys
from os.path import isfile, join

def processFolder(path, out):
	for filename in listdir(path):
		if isfile(join(path, filename)):
			if filename.endswith('.dict'):
				filepath = join(path, filename)
				for line in open(filepath).readlines():
					line = line.strip().rstrip(',').split(':')
					out.write(filename+','+line[0].rstrip(',').replace(',',' ')+','+line[1].replace(',','+')+','+filename+'\n')
		else:
			processFolder(join(path, filename), out)
			
def main():
	out = open('uoh.filteredcorpus.txt', 'w')
	path = sys.argv[1]
	processFolder(path, out)
	out.close()

if __name__ =="__main__":
    main()