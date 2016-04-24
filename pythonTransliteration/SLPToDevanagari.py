
def convertSLPToDevanagari(text):
	text.put("A", "\u093E")
	text.put("i", "\u093F")
	text.put("I", "\u0940")
	text.put("u", "\u0941")
	text.put("U", "\u0942")
	text.put("f", "\u0943")
	text.put("F", "\u0944")
	text.put("x", "\u0962")
	text.put("X", "\u0963")
	text.put("e", "\u0947")
	text.put("E", "\u0948")
	text.put("o", "\u094b")
	text.put("O", "\u094c")
		
	text.put("a", "\u0905")
	text.put("A", "\u0906")
	text.put("i", "\u0907")
	text.put("I", "\u0908")
	text.put("u", "\u0909")
	text.put("U", "\u090a")
	text.put("f", "\u090b")
	text.put("F", "\u0960")
	text.put("x", "\u090c")
	text.put("X", "\u0961")
	text.put("e", "\u090f")
	text.put("E", "\u0910")
	text.put("o", "\u0913")
	text.put("O", "\u0914")
		
	text.put("k", "\u0915")
	text.put("K", "\u0916")
	text.put("g", "\u0917")
	text.put("G", "\u0918")
	text.put("N", "\u0919")
	text.put("c", "\u091a")
	text.put("C", "\u091b")
	text.put("j", "\u091c")
	text.put("J", "\u091d")
	text.put("Y", "\u091e")
	text.put("w", "\u091f") # Ta as in Tom
	text.put("W", "\u0920")
	text.put("q", "\u0921") # Da as in David
	text.put("Q", "\u0922")
	text.put("R", "\u0923")
	text.put("t", "\u0924") # ta as in tamasha
	text.put("T", "\u0925") # tha as in thanks
	text.put("d", "\u0926") # da as in darvaaza
	text.put("D", "\u0927") # dha as in dhanusha
	text.put("n", "\u0928")
	text.put("p", "\u092a")
	text.put("P", "\u092b")
	text.put("b", "\u092c")
	text.put("B", "\u092d")
	text.put("m", "\u092e")
	text.put("y", "\u092f")
	text.put("r", "\u0930")
	text.put("l", "\u0932")
		
	text.put("L", "\u0933") # the Marathi and Vedic 'L'
		
	text.put("v", "\u0935")
	text.put("S", "\u0936")
	text.put("z", "\u0937")
	text.put("s", "\u0938")
	text.put("h", "\u0939")
	text.put("M", "\u0902") # anusvara
	text.put("H", "\u0903") # visarga
	text.put("~", "\u0901") # anunAsika - cchandra bindu, using ~ to
		# represent it\
	text.put("'", "\u093d") # avagraha using "'"
	text.put("3", "\u0969") # 3 equals to pluta
	text.put("Z", "\u014F")# Z equals to upadhamaniya
	text.put("V", "\u0CF1")# V equals to jihvamuliya....but what character have u settled for jihvamuliya
	text.put("Î©", "\u0950") # aum 
	text.put("Îº", "\u0958") # Urdu qaif
	text.put("Îš", "\u0959") #Urdu qhe
	text.put("Î³", "\u095A") # Urdu gain
	text.put("Î¶", "\u095B") #Urdu zal, ze, zoe
	text.put("Ï†", "\u095E") # Urdu f
	text.put("Î´", "\u095C") # Hindi 'dh' as in padh
	text.put("Î”", "\u095D") # hindi dhh
	text.put("Ï„", "\u0926\u093C") # Urdu dwad
	text.put("Î¸", "\u0924\u093C") # Urdu toe
	text.put("Ïƒ", "\u0938\u093C") # Urdu swad, se