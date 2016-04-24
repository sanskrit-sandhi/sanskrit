# -*- coding: utf-8 -*-
out = open('mw.words.out', 'w')
for line in open('mw_orig_utf8.txt').xreadlines():
	line = line.strip()
	if "<H1>100{" in line:
		word = line.split('{')[1].split('}')[0].split(' ')[0].split('(')[0].split(',')[0].split('.')[0].split('/')[0].split('\\')[0].split('-')[0].split('{')[0].replace("'","").replace('*','').replace('†','').replace('[','').replace('?','')
		out.write(word+'\n');
out.close()
