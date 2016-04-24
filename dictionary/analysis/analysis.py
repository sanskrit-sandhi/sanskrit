from sets import Set
fileDict = {'ap90' :'ap90.words.out.out',
	'bhs' :'bhs.words.out.slp.out.out',
	'gst' :'gst.words.out.out',
	'mw' :'mw.words.out.slp.out.out',
	'shs' :'shs.words.out.slp.out.out',
	'yat' :'yat.words.out.out',
	'ben' :'ben.words.out.out',
	'cae' :'cae.words.out.out',
	'md' :'md.words.out.out',
	'mw72' :'mw72.words.out.out',
	'wil' :'wil_orig.words.out.out'}

def getSet(file):
	se = Set([])
	for line in open(file).xreadlines():
		line = line.strip()
		se.add(line)
	return se

setDict = {}
skd = getSet('skd.words.out.out');
vcp= getSet('vcp.words.out.out');
skdandvcp = skd & vcp;
skdorvcp = skd | vcp;
onlyskd = skd - vcp;
onlyvcp = vcp - skd;
#print skdandvcp
diffDict = {}
for (key, val) in fileDict.iteritems():
	set = getSet(val)
	diffDict[key+'&skd'] = set & skd
	diffDict[key+'&vcp'] = set & vcp
	diffDict[key+'|skd'] = set | skd
	diffDict[key+'|vcp'] = set | vcp
	diffDict[key+'&skd&vcp'] = set & skd & vcp
	diffDict[key+'-skd-vcp'] = set - skd - vcp
	diffDict['skd-vcp-'+key] = skd - vcp - set
	diffDict['vcp-skd-'+key] = vcp - skd - set
	diffDict['vcp+skd+'+key]  = vcp | skd | set
	
for(key,val) in diffDict.iteritems():
	out = open(key+'.diff', 'w');
	for va in val:
		out.write(va+'\n');
	out.close()
	
out = open('skd&vcp.diff', 'w')
for va in skdandvcp:
	out.write(va+'\n');
out.close()
out = open('skd|vcp.diff', 'w')
for va in skdorvcp:
	out.write(va+'\n');
out.close()
out = open('skd-vcp.diff', 'w')
for va in onlyskd:
	out.write(va+'\n');
out.close()
out = open('vcp-skd.diff', 'w')
for va in onlyvcp:
	out.write(va+'\n');
out.close()