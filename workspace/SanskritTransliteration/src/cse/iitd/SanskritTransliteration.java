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

public class SanskritTransliteration {
	public static void main(String[] args) throws IOException {
		// String data =
		// convertFromFile("C:\\Users\\IBM_ADMIN\\Desktop\\sanskrit\\python\\input.txt");
		// System.out.println(EncodingUtil.convertDevanagariToSLP(data).replaceAll("#####",
		// "\n"));
		
		String inputFile = "C:\\Users\\IBM_ADMIN\\Desktop\\IITD\\sanskritResources\\dictionary\\sanskrit-sanskrit\\";
		//String outputFile = "C:\\Users\\IBM_ADMIN\\Desktop\\sanskritResources\\dictionary\\";
		//String inputFile = "C:\\Users\\IBM_ADMIN\\Desktop\\sanskrit\\python\\output.txt";
		//String outputFile = "C:\\Users\\IBM_ADMIN\\Desktop\\sanskrit\\python\\output1.txt";
		String inputCharSet = "SLP";
		String outputCharSet = "DVN";
		//String[] sec = {"bentxt//ben.words.out","gsttxt//gst.words.out","mw72txt//mw72.words.out","wiltxt//wil_orig.words.out","yattxt//yat.words.out"};
		//String[] thr = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"};
		//String[] sec = {"ap90txt//ap90.words.out","bhstxt//bhs.words.out","caetxt//cae.words.out","mdtxt//md.words.out","mwtxt//mw.words.out","shstxt//shs.words.out"};
		String[] sec = {"skdtxt//skd.words.out","vcptxt//vcp.words.out"};
		/*String[] sec = {"ap90.words.out", "bhs.words.out", "gst.words.out", "mw.words.out", "sans-eng.all.out", "shs.words.out", "vcp.words.out", 
				"yat.words.out", "ben.words.out", "cae.words.out", "md.words.out", "mw72.words.out", "sans-sans.all.out", "skd.words.out", "wil_orig.words.out"};*/
		//String[] sec = {"bentxt//ben.words.out"};
		
		/*for(String se : sec){
			String inFile = inputFile+se ;
			String outFile = inFile +".slp";
			System.out.println(inFile);
			String data = convertFromFile(inFile);
			String transData = "";
			for (String line: data.split("#####")) {
				transData = transData + EncodingUtil.convertIAST1ToSLP(line)+"\n";
			}
			writeToFile(transData, outFile);
	}*/
		
		for(String se : sec){
				String inFile = inputFile+se;
				String outFile = inFile +".out";
				System.out.println(inFile);
				String data = convertFromFile(inFile);
				String transData = "";
				for (String line: data.split("#####")) {
					transData = transData + EncodingUtil.convertToDVN(line, inputCharSet)+"\n";
				}
				writeToFile(transData, outFile);
		}
		
		System.out.println(EncodingUtil.convertSLPToDevanagari("paMKa"));

		/*if (args.length > 5){
			inputFile = args[1];
			outputFile = args[2];
			inputCharSet = args[3];
			outputCharSet = args[4];
		}
		
		if (outputCharSet.equalsIgnoreCase("DVN")) {
			String data = convertFromFile(inputFile);
			String transData = EncodingUtil.convertToDVN(data, inputCharSet).replaceAll("#####", "\n");
			writeToFile(transData, outputFile);
		} else if (outputCharSet.equalsIgnoreCase("SLP")) {
			String data = convertFromFile(inputFile);
			String transData = EncodingUtil.convertToSLP(data, inputCharSet).replaceAll("#####", "\n");
			writeToFile(transData, outputFile);
		} else if (outputCharSet.equalsIgnoreCase("IAST")) {
			String data = convertFromFile(inputFile);
			String transData = EncodingUtil.convertToIAST(data, inputCharSet)	.replaceAll("#####", "\n");
			writeToFile(transData, outputFile);
		} */
	}

	public static String convertFromFile(String filePath) throws IOException {
		File fileDir = new File(filePath);

		BufferedReader in = new BufferedReader(new InputStreamReader(
				new FileInputStream(fileDir), "UTF8"));

		String str;
		String data = "";
		while ((str = in.readLine()) != null) {
			data = data + "#####" + str;
		}
		in.close();
		return data;
	}

	public static void writeToFile(String data, String outFile) throws IOException {
		Writer out = new BufferedWriter(new OutputStreamWriter(
				new FileOutputStream(outFile), "UTF-8"));
		out.write(data);
		out.close();

	}
}
