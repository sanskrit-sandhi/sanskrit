# coding=utf-8
def convert(value):
	inHex = [ "05", "06", "07", "08", "09", "0a", "0b", "60", "0c", "0f", "10", "13", "14", "02", "01", "03", "3d", "4d" ]
	outVH = [ "a", "aa", "i", "ii", "u", "uu", ".r", ".rr", ".l", "e", "ai", "o", "au", ".m", "~l", ".h", "'", "" ]
	matIn = [ "3e", "3f", "40", "41", "42", "43", "44", "62", "47", "48", "4b", "4c" ]
	consIn = [ "15", "16", "17", "18", "19", "1a", "1b", "1c", "1d", "1e", "1f", "20", "21", "22", "23", "24", "25", "26", "27", "28", "2a", "2b", "2c", "2d", "2e", "2f", "30", "32", "35", "36", "37", "38", "39", "00" ]
	orig = value.strip().decode("utf-8")
	output = ""
	wasCons = False
	for i in range(len(orig)):
	
		origC = orig[i]
		l = "{0:04x}".format(ord(origC))
		
		lenL = len(l)
		if lenL == 0:
			l = "0000"
		if lenL == 1:
			l = "000" + l
		if lenL == 2:
			l = "00" + l
		if lenL == 3:
			l = "0" + l
		check = l[2:]
		init = l[0:2]
		
		if not init == "09":
			check = "00"

		consOut = [ "k", "kh", "g", "gh", "f", "c", "ch", "j", "jh", "~n", ".t", ".th", ".d", ".dh", ".n", "t", "th", "d", "dh", "n", "p", "ph", "b", "bh", "m", "y", "r", "l", "v", "z", ".s", "s", "h", origC + "" ]
		for j in range (len(inHex)):
			if check == inHex[j]:
				if check == "03" or check == "01" or check == "02" or check == "3d":
					if wasCons:
						output = output+"a" + outVH[j]
					else:
						output = output+outVH[j]
				else:
					output = output+outVH[j]
				wasCons = False
		for j in range (len(consIn)):
			if check == consIn[j]:
				if wasCons:
					output = output+"a" + consOut[j]
				else:
					output = output+consOut[j]
				if not check == "00":
					wasCons = True
				else:
					wasCons = False
				if i == len(orig) - 1:
					output = output+"a"
		for j in range (len(matIn)):
			if check == matIn[j]:
				output = output+outVH[j + 1]
				wasCons = False
	return output
print convert("चार्थे")