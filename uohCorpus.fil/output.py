import sys
def process(file):	
	jnuMap = {}
	inriaMap = {}
	inriaFilMap = {}
	samMap = {}
	samFilMap = {}
	out = open(file+'.out','w')
	gar = open('garbage.out','w')
	for line in open(file+'.jnu.cor').readlines():
		line = line.strip().split(':')
		jnuMap[line[0]] = '1'
	for line in open(file+'.inria.cor').readlines():
		line = line.strip().split(':')
		inriaMap[line[0]] = '1'
	for line in open(file+'.inria.fil.cor').readlines():
		line = line.strip().split(':')
		inriaFilMap[line[0]] = '1'
	for line in open(file+'.sam.cor').readlines():
		line = line.strip().split(':')
		samMap[line[0]] = '1'
	for line in open(file+'.sam.fil.cor').readlines():
		line = line.strip().split(':')
		samFilMap[line[0]] = '1'
		
	for line in open(file).readlines():
		lineArr = line.strip().split(',')
		if lineArr[1].replace(' ','') != lineArr[2].replace('+','').replace(' ','') and len(lineArr[2].split('+')) > 1:
			out.write(line.strip())
			if jnuMap.has_key(lineArr[0]):
				out.write(','+jnuMap[lineArr[0]])
			else:
				out.write(',');
			if inriaMap.has_key(lineArr[0]):
				out.write(','+inriaMap[lineArr[0]])
			else:
				out.write(',');
			if inriaFilMap.has_key(lineArr[0]):
				out.write(','+inriaFilMap[lineArr[0]])
			else:
				out.write(',');
			if samMap.has_key(lineArr[0]):
				out.write(','+samMap[lineArr[0]])
			else:
				out.write(',');
			if samFilMap.has_key(lineArr[0]):
				out.write(','+samFilMap[lineArr[0]])
			else:
				out.write(',');
			out.write('\n')
		else:
			gar.write(line.strip())
			if jnuMap.has_key(lineArr[0]):
				gar.write(','+jnuMap[lineArr[0]])
			else:
				gar.write(',');
			if inriaMap.has_key(lineArr[0]):
				gar.write(','+inriaMap[lineArr[0]])
			else:
				gar.write(',');
			if inriaFilMap.has_key(lineArr[0]):
				gar.write(','+inriaFilMap[lineArr[0]])
			else:
				gar.write(',');
			if samMap.has_key(lineArr[0]):
				gar.write(','+samMap[lineArr[0]])
			else:
				gar.write(',');
			if samFilMap.has_key(lineArr[0]):
				gar.write(','+samFilMap[lineArr[0]])
			else:
				gar.write(',');
			gar.write('\n')
	out.close()
	gar.close()
def main():
    path = sys.argv[1]
    process(path)

if __name__ =="__main__":
    main()