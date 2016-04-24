def HKTToSLP(text):
	text = text.replaceAll("ai", "E");
	text = text.replaceAll("au", "O");
	text = text.replaceAll("IRR", "X");
	text = text.replaceAll("IR", "x");
	text = text.replaceAll("RR", "F");
	text = text.replaceAll("R", "f");
	text = text.replaceAll("N", "R");
	text = text.replaceAll("G", "N");
	text = text.replaceAll("J", "Y"); 
	text = text.replaceAll("kh", "K");
	text = text.replaceAll("gh", "G");
	text = text.replaceAll("ch", "C");
	text = text.replaceAll("jh", "J");
	text = text.replaceAll("Th", "W");  
	text = text.replaceAll("T", "w");
	text = text.replaceAll("Dh", "Q");  
	text = text.replaceAll("D", "q");
	text = text.replaceAll("th", "T");
	text = text.replaceAll("dh", "D");
	text = text.replaceAll("ph", "P");
	text = text.replaceAll("bh", "B");
	text = text.replaceAll("z", "@@"); //'@@' is a temporary holder.
	text = text.replaceAll("S", "z");
	text = text.replaceAll("@@", "S");
	text = text.replaceAll("\\.a", "'"); 
	text = text.replaceAll("\\.N", "~"); 
	return text;
