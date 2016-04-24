# -*- coding: utf-8 -*-
out = open('ap90.words.out', 'w')
for line in open('ap90_orig_utf8_slp1.txt').xreadlines():
	line = line.strip()
	if "<P>.{#" in line:
		word = line.split('{#')[1].split('#}')[0].split(' ')[0].split('(')[0].split(',')[0].split('.')[0].split('/')[0].split('\\')[0].split('-')[0].split('{')[0].replace("'","").replace('*','').replace('†','').replace('[','').replace('?','')
		out.write(word+'\n');
out.close()
