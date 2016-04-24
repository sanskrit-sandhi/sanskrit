# -*- coding: utf-8 -*-
out = open('skd.words.out', 'w')
for line in open('skd_orig_utf8_slp1.txt').xreadlines():
	line = line.strip()
	if "<HI>" in line:
		word = line.split('<HI>')[1].split(',')[0].split(' ')[0].split('(')[0].split(',')[0].split('.')[0].split('/')[0].split('\\')[0].split('-')[0].split('{')[0].replace("'","").replace('*','').replace('†','').replace('[','').replace('?','')
		out.write(word+'\n');
out.close()
