def convertSLPToHK(text):
	text = text.replace("N","0")  
	text = text.replace("Y","1")  
	text = text.replace("R","N")
	text = text.replace("f", "R")    
	text = text.replace("F","RR")# same reason as above
	text = text.replace("x","IR")
	text = text.replace("X","IRR")

	text = text.replace("E","ai")
	text = text.replace("O","au")

	text = text.replace("K","kh")
	text = text.replace("G","gh")

	text = text.replace("C","ch")
	text = text.replace("J","jh") 

	text = text.replace("T","th")
	text = text.replace("D","dh")
	text = text.replace("w","T")
	text = text.replace("W","Th")
	text = text.replace("q","D")
	text = text.replace("Q","Dh")


	text = text.replace("P","ph") 
	text = text.replace("B","bh")
	text = text.replace("S","Z")
	text = text.replace("z","S") 
	text = text.replace("Z","z") 
	text = text.replace("'", ".a")    # avagraha

	text = text.replace("0","G")  
	text = text.replace("1","J") 

	return text # return text
