from os import listdir
import sys
from os.path import isfile, join


dict = []
for line in open('words.all.txt').xreadlines():
	line = line.strip()
	dict.append(line)
	
	
def processFolder(path):
	for filename in listdir(path):
		if isfile(join(path, filename)):
			if filename.endswith('.txt.out'):
				filepath = join(path, filename)
				out = open(filepath+'.dict', 'w')
				for line in open(filepath).xreadlines():
					flag = True
					line = line.strip()
					splits = line.split(':')[1].split(',')
					for split in splits:
						if len(split)!=0 and not split.strip() in dict:
							flag = False
							break
					if flag:
						out.write(line+'\n');
				out.close()
		else:
			processFolder(join(path, filename))
		
def main():
    path = sys.argv[1]
    processFolder(path)

if __name__ =="__main__":
    main()