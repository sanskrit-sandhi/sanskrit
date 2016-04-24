
def convertSLPToItrans(text):
	text = text.replace("f", "6") # if I make f == "RRi" 
	text = text.replace("N","5") # N (kvargIya) -> 5 -> ~N 
	text = text.replace("R","N")# confusion with .replace("N","~N"), ref. note 1
	#text = text.replace("f", "RRi")	
	text = text.replace("F","7")# same reason as above
	text = text.replace("x","LLi")
	text = text.replace("X","LLI")
	text = text.replace("E","ai")
	text = text.replace("O","au")
	text = text.replace("K","kh")
	text = text.replace("G","gh")
    text = text.replace("c","ch")
	text = text.replace("C","Ch")
	text = text.replace("J","jh") 
	text = text.replace("Y","~n")
	text = text.replace("T","th")
	text = text.replace("D","dh")
	text = text.replace("w","T")
	text = text.replace("W","Th")
	text = text.replace("q","D")
	text = text.replace("Q","Dh")
	text = text.replace("P","ph") 
	text = text.replace("B","bh")
	text = text.replace("S","sh")
	text = text.replace("z","Sh")
	text = text.replace("~",".N") # chandrabindu 
	text = text.replace("'", ".a")	# avagraha
	text = text.replace("5","~N") # refer to NOTE 1, 5 -> ~N ( kavargIya )
	text = text.replace("6", "RRi")
	text = text.replace("7", "RRI")
	return text # return text
