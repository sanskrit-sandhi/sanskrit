def convertSLPToIAST(text):
	text.replace("Î©", "\u0950") # aum 
	text.replace("Îº", "q") # Urdu qaif
	text.replace("Îš", "qh") #Urdu qhe
	text.replace("Î³", "g" ) # Urdu gain
	text.replace("Î¶", "z") #Urdu zal, ze, zoe
	text.replace("Ï†", "f") # Urdu f
	text.replace("Î´",  "á¹›" ) # Hindi 'dh' as in padh
	text.replace("Î”",  "á¹�" + "h") # hindi dhh
	text.replace("Ï„", "d") # Urdu dwad
	text.replace("Î¸", "t") # Urdu toe
	text.replace("Ïƒ", "s") # Urdu swad, se


	text.replace("A","Ä�" /*"a" + bar_above*/) # a + bar above
	# text.replace("i", "\u0907")
	text.replace("I", "Ä«")# i + bar above
	# text.replace("u", "\u0909")
	text.replace("U", "Å«")# u + bar above
	text.replace("f", "á¹›") # r + dot below
	text.replace("F", "á¹�") # r + dot below and bar
	# above
	text.replace("x", "á¸·") # l + dot below
	text.replace("X", "á¸¹") # l + dot below and bar
	# above
	text.replace("E", "ai")
	text.replace("O", "au")

	text.replace("K", "kh")
	text.replace("G", "gh")
	text.replace("N", "á¹…") # n + dot above
	text.replace("C", "ch")
	text.replace("J", "jh")
	text.replace("Y", "Ã±") # n + bar above
	text.replace("w", "á¹­") # t + dot below # Ta as in Tom
	text.replace("W", "á¹­h") # t + dot below
	text.replace("q", "á¸�") # t + dot below # Da as in David
	text.replace("Q", "á¸�h") # t + dot below
	text.replace("R", "á¹‡") # n + dot below
	# text.replace("t", "\u0924") # ta as in tamasha
	text.replace("T", "th") # tha as in thanks
	# text.replace("d", "\u0926") # da as in darvaaza
	text.replace("D", "dh") # dha as in dhanusha
	# text.replace("n", "\u0928")
	# text.replace("p", "\u092a")
	text.replace("P", "ph")
	# text.replace("b", "\u092c")
	text.replace("B", "bh")
	# text.replace("m", "\u092e")
	# text.replace("y", "\u092f")
	# text.replace("r", "\u0930")
	# text.replace("l", "\u0932")
	# text.replace("v", "\u0935")
	text.replace("S", "Å›") # slash above
	text.replace("z", "á¹£")
	# text.replace("s", "\u0938")
	# text.replace("h", "\u0939")
	text.replace("M", "á¹ƒ") # anusvara
	text.replace("H","á¸¥") # visarga
	text.replace("~", "\u0310") # anunAsika - cchandra bindu, using ~ to
		# represent it\
	# text.replace("'", "\u093d") # avagraha using "'" : same in extended
	# latin
	# text.replace("3", "\u0969") # 3 equals to pluta
	# text.replace("8", "\u014F")#8 equals to upadhamaniya
	return text