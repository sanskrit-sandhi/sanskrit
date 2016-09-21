import sys
def process(file):	
	jnuMap = {}
	inriaMap = {}
	inriaFilMap = {}
	samMap = {}
	samFilMap = {}
	out = open(file+'.out','w')
	for line in open(file+'.jnu').readlines():
		line = line.strip().split(':')
		print line[0], line[7]
		jnuMap[line[0]] = line[7]
	for line in open(file+'.ext.inria').readlines():
		line = line.strip().split(':')
		inriaMap[line[0]] = line[7]
	for line in open(file+'.int.inria').readlines():
		line = line.strip().split(':')
		inriaFilMap[line[0]] = line[7]
	for line in open(file+'.uoh').readlines():
		line = line.strip().split(':')
		samMap[line[0]] = line[7]
		
	for line in open(file).readlines():
		lineArr = line.strip().split(',')[0].split(':')
		out.write(line.strip())
		print lineArr[0]
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
		out.write('\n')
def main():
    path = sys.argv[1]
    process(path)

if __name__ =="__main__":
    main()
