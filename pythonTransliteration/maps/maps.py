# -*- coding: utf-8 -*-

dicts = {'dev':["अ", "आ", "इ", "ई", "उ", "ऊ", "ऋ", "ॠ", "ऌ", "ॡ", "ए", "ऐ", "ओ", "औ", "ा", "ि", "ी", "ु", "ू", "ृ", "ॄ", "ॢ", "ॣ", "े", "ै", "ो", "ौ", "्", "ं", "ः", "ँ", "ॅ", "क", "ख", "ग", "घ", "ङ", "च", "छ", "ज", "झ", "ञ", "ट", "ठ", "ड", "ढ", "ण", "त", "थ", "द", "ध", "न", "प", "फ", "ब", "भ", "म", "य", "र", "ल", "व", "श", "ष", "स", "ह", "ळ", "क्ष", "ज्ञ", "क़", "ख़", "ग़", "ज़", "ड़", "ढ़", "फ़", "य़", "ऱ", "ॐ", "ऽ", "।", "॥", "॒", "॑", "०", "१", "२", "३", "४", "५", "६", "७", "८", "९", ""],

'Iast':["a", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ", "e", "ai", "o", "au", "ā", "i", "ī", "u", "ū", "ṛ", "ṝ", "ḷ", "ḹ", "e", "ai", "o", "au", "", "ṃ", "ḥ", "m̐", "", "k", "kh", "g", "gh", "ṅ", "c", "ch", "j", "jh", "ñ", "ṭ", "ṭh", "ḍ", "ḍh", "ṇ", "t", "th", "d", "dh", "n", "p", "ph", "b", "bh", "m", "y", "r", "l", "v", "ś", "ṣ", "s", "h", "ḻ", "kṣ", "jñ", "", "", "", "", "", "", "", "", "", "oṃ", "'", "।", "॥", "", "", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ""],

'Hk':["a", "A", "i", "I", "u", "U", "R", "RR", "lR", "lRR", "e", "ai", "o", "au", "A", "i", "I", "u", "U", "R", "RR", "lR", "lRR", "e", "ai", "o", "au", "", "M", "H", "", "", "k", "kh", "g", "gh", "G", "c", "ch", "j", "jh", "J", "T", "Th", "D", "Dh", "N", "t", "th", "d", "dh", "n", "p", "ph", "b", "bh", "m", "y", "r", "l", "v", "z", "S", "s", "h", "L", "kS", "jJ", "", "", "", "", "", "", "", "", "", "OM", "'", "|", "||", "", "", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ""],

'Itrans':["a", "A", "i", "I", "u", "U", "RRi", "RRI", "LLi", "LLI", "e", "ai", "o", "au", "A", "i", "I", "u", "U", "RRi", "RRI", "LLi", "LLI", "e", "ai", "o", "au", "", "M", "H", ".N", ".c", "k", "kh", "g", "gh", "~N", "ch", "Ch", "j", "jh", "~n", "T", "Th", "D", "Dh", "N", "t", "th", "d", "dh", "n", "p", "ph", "b", "bh", "m", "y", "r", "l", "v", "sh", "Sh", "s", "h", "L", "kSh", "j~n", "q", "K", "G", "z", ".D", ".Dh", "f", "Y", "R", "OM", ".a", "|", "||", "\\_", "\\'", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "{}"],

'Itrans2':["a", "aa", "", "ii", "", "uu", "R^i", "R^I", "L^i", "L^I", "", "", "", "", "aa", "", "ii", "", "uu", "R^i", "R^I", "L^i", "L^I", "", "", "", "", ".h", ".m", "", "", "", "", "", "", "", "N^", "c", "C", "", "", "JN", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "w", "", "shh", "", "", "", "x", "GY", "", "", "", "J", "", "", "", "", "", "AUM", "~", ".", "..", "", "", "", "", "", "", "", "", "", "", "", "", "_"],

'Slp':["a", "A", "i", "I", "u", "U", "f", "F", "x", "X", "e", "E", "o", "O", "A", "i", "I", "u", "U", "f", "F", "x", "X", "e", "E", "o", "O", "", "M", "H", "~", "", "k", "K", "g", "G", "N", "c", "C", "j", "J", "Y", "w", "W", "q", "Q", "R", "t", "T", "d", "D", "n", "p", "P", "b", "B", "m", "y", "r", "l", "v", "S", "z", "s", "h", "L", "kz", "jY", "", "", "", "", "", "", "", "", "", "oM", "'", ".", "..", "", "", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ""],

'Sanskritocr':["a", "å", "i", "ï", "u", "÷", "Ÿ", "", "", "", "e", "ai", "o", "au", "å", "i", "ï", "u", "÷", "Ÿ", "", "", "", "e", "ai", "o", "au", "", "º", "µ", "", "", "k", "kh", "g", "gh", "¼", "c", "ch", "j", "jh", "ñ", "¶", "¶h", "·", "·h", "½", "t", "th", "d", "dh", "n", "p", "ph", "b", "bh", "m", "y", "r", "l", "v", "¸", "¹", "s", "h", "", "k¹", "jñ", "", "", "", "", "", "", "", "", "", "", "'", "/", "//", "", "", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ""],

'Iast1': ["a", "a1", "i", "i1", "u", "u1", "r2", "r21", "l2", "l21", "e", "ai", "o", "au", "a1", "i", "i1", "u", "u1", "r2", "r21", "l2", "l21", "e", "ai", "o", "au", "", "m2", "h2", "m̐", "", "k", "kh", "g", "gh", "n3", "c", "ch", "j", "jh", "n5", "t2", "t2h", "d2", "d2h", "n2", "t", "th", "d", "dh", "n", "p", "ph", "b", "bh", "m", "y", "r", "l", "v", "s4", "s2", "s", "h", "l2", "ks2", "jn5", "", "", "", "", "", "", "", "", "", "om2", "'", "।", "॥", "", "", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ""]

}

for key, value in dicts.iteritems():
	for key1, value1 in dicts.iteritems():
		if key != key1:
			out = open(key+'_'+key1+'.map','w')
			for i in range(0, len(value)):
				out.write(value[i]+':'+value1[i]+'\n')
			out.close()

