package cse.iitd;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.Writer;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SandhiType {
	private static final List<String> vowels = Arrays.asList("a", "A", "i", "I", "u", "U", "f", "F", "x", "X", "e", "E", "o", "O", "aM", "aH", "a????");
	public static boolean isVowelChar(String alphabet){
	    if (vowels.contains(alphabet))
	        return true;
	    return false;
	}
	public static boolean isStartsWithVowel(String word){
	   String firstLetter = word.substring(0,1);
	   return isVowelChar(firstLetter);
	}
	
	public static boolean isEndsWithVowel(String word){
		String lastLetter = word.substring(word.length()-1);
		return isVowelChar(lastLetter);
	}


	  public static boolean isEndsWithVisarga(String word){
	    return word.substring(word.length()-1).equals("H");
	  }
	  private static Boolean isVisargaSandhi(String word) {
		  if(isEndsWithVisarga(word))
		        return true;
			return false;
		}
		private static Boolean isVowelSandhi(String word1, String word2) {
			if (isEndsWithVowel(word1) && isStartsWithVowel(word2))
				return true;
			return false;
		}

		private static boolean isCumTrue(List<Boolean> list){
		    Boolean result = true;
		    if (list.size() > 0){
		        for(Boolean i : list)
		            result = result && i;
		        return result;
		    }
		    return false;
		}

	public static String sandhiType(String words){
	    String[] wordSplit = words.trim().split("\\+");
	    List<Boolean> isVowel = new ArrayList<>();
	    List<Boolean> isVisarga = new ArrayList<>();
	    for(int i=0; i<wordSplit.length-1; i++){
	    	String word1 = EncodingUtil.convertDevanagariToSLP(wordSplit[i]);
	        String word2 = EncodingUtil.convertDevanagariToSLP(wordSplit[i+1]);
	        System.out.println(word1+" : "+word2);
	        isVowel.add(isVowelSandhi(word1, word2));
	        isVisarga.add(isVisargaSandhi(word1));
	    }
	    if(isCumTrue(isVowel))
			return ",1,0,0\n";   //Consonent Sandhi
		else if(isCumTrue(isVisarga))
			return ",0,1,0\n";   //Visarga Sandhi
		return ",0,0,1\n"; //Consonant Sandhi
	}
	
	public static void convertFromFile(String filePath) throws IOException {
		File fileDir = new File(filePath);
		String outFile = filePath+".type";
		BufferedReader in = new BufferedReader(new InputStreamReader(new FileInputStream(fileDir), "UTF8"));
		Writer out = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(outFile), "UTF-8"));

		String str;
		
		while ((str = in.readLine()) != null) {
			System.out.println(str.split(",")[0]);
			String split = str.split(",")[2];
			String type = sandhiType(split);
			out.write(str+type);
		}
		in.close();
		out.close();
	}

	public static void convertFromFolder(String folderPath) throws IOException {
		File folder = new File(folderPath);
		if(folder.isDirectory())
		    for (final File fileEntry : folder.listFiles()) {
		        if (fileEntry.isDirectory()) {
		        	convertFromFolder(fileEntry.getAbsolutePath());
		        } else {
		        	convertFromFile(fileEntry.getAbsolutePath());
		        }
		    }
		else convertFromFile(folderPath);
	}
	    

	
	public static void main(String[] args) throws IOException {
		//System.out.println(sandhiType("एव+इत्यादि"));
		//System.out.println(sandhiType("अज्ञातवासः+च "));
		//convertFromFile("/Users/neelamadhav/Desktop/IBM_old/IITD/sanskritResources/sanskrit/sandhiTypes/Literature.txt.nospace");
		//convertFromFile("/Users/neelamadhav/Desktop/IBM_old/IITD/sanskritResources/sanskrit/sandhiTypes/Literature.txt.plus");
		convertFromFile("/Users/neelamadhav/Desktop/IBM_old/IITD/sanskritResources/sanskrit/sandhiTypes/astadhayi.txt");
		convertFromFile("/Users/neelamadhav/Desktop/IBM_old/IITD/sanskritResources/sanskrit/sandhiTypes/gitaCorpus.txt.nospace");
		convertFromFile("/Users/neelamadhav/Desktop/IBM_old/IITD/sanskritResources/sanskrit/sandhiTypes/gitaCorpus.txt.plus");
		convertFromFile("/Users/neelamadhav/Desktop/IBM_old/IITD/sanskritResources/sanskrit/sandhiTypes/golddataset.txt");
		convertFromFile("/Users/neelamadhav/Desktop/IBM_old/IITD/sanskritResources/sanskrit/sandhiTypes/uoh.filteredcorpus.txt");
		//convertFromFile("/Users/neelamadhav/Desktop/IBM_old/IITD/sanskritResources/sanskrit/sandhiTypes/test.txt");

	}

}
