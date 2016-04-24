def convertItransToUniformIrans(text):
	text = text.replaceAll("x", "kSh");
	text = text.replaceAll("GY", "j~n");
	text = text.replaceAll("dny", "j~n");
	text = text.replaceAll("w", "v");
	text = text.replaceAll("[\\.][a]", "'"); 
	text = text.replaceAll("aa", "A");
	text = text.replaceAll("ii", "I");
	text = text.replaceAll("uu", "U");

	text = text.replaceAll("R\\^i", "RRi");
	text = text.replaceAll("R\\^I", "RRI");
	text = text.replaceAll("L\\^i", "LLi");
	text = text.replaceAll("L\\^I", "LLI");
	text = text.replaceAll("Ch", "C"); // must be above
	text = text.replaceAll("ch", "c");

	text = text.replaceAll("N\\^", "~N");
	text = text.replaceAll("JN", "~n");

	text = text.replaceAll("w", "v");


	text = text.replaceAll("\\.n", "M");
	text = text.replaceAll("\\.m", "M");
	return text;