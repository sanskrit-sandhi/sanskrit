import sys
import codecs
import DvnToSLP
import chardet
separators = [u"?", u",", u".", u"|", ]



def translate(inFile, outFile):
	#lines = open(inFile).read()
	out = 	codecs.open(outFile, 'w', encoding='utf-8')
	file = codecs.open(inFile, encoding='latin1')
	for line in file:
		print chardet(line);
		text = line
		slp = DvnToSLP.convertDvnToSLP(text)
		out.write(slp.encode("latin1").decode('utf-8'))
	out.close()
			
	

def main():
	'''if len(sys.argv) < 5:
		print "Usage run.py input.txt output.txt inputLang outputLand"
		exit(0)
	inputFile = sys.argv[1]
	outputFile = sys.argv[2]
	inputType = sys.argv[3]
	outputType = sys.argv[4]'''
	inFile = 'C:/Users/IBM_ADMIN/Desktop/sanskrit/python/input.txt'
	outFile = 'C:/Users/IBM_ADMIN/Desktop/sanskrit/python/input.txt.out'
	translate(inFile, outFile);

	
if __name__=='__main__':
	main()