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
import java.util.List;

public class SandhiTesting {

	public static void main(String[] args) throws IOException {
		
		//String test = "C:\\Users\\IBM_ADMIN\\Desktop\\sanskritResources\\sandhiTesting\\test.txt";
		//convertFile(test);
		//String inputFile = "C:\\Users\\IBM_ADMIN\\Desktop\\sanskritResources\\sandhiTesting\\vinodini-ext.txt";
		//convertFile(inputFile);
		
		String folderPath = "C:\\Users\\IBM_ADMIN\\Desktop\\IITD\\sanskritResources\\sandhiTesting\\";
		convertFolder(folderPath);

	}
	
	public static void convertFolder(String folderPath) throws IOException {
		File folder = new File(folderPath);
		if (folder.isDirectory()) {
			File[] files = folder.listFiles();
			for (File file : files) {
				if (file.isDirectory()) {
					convertFolder(file.getAbsolutePath());
				} else {
					convertFile(file.getAbsolutePath());
				}
			}
		} else
			convertFile(folderPath);
	}
	
	public static void writeToFile(List<String> left, List<String> right, Writer out, Writer out1) throws IOException {
		//System.out.println(left.toString()+" "+right.toString());
		//out.write(left.toString() +":" + right.toString());
		for(String le:left)
			if(!"".equals(le) && !",".equals(le))
				out.write(le.replaceAll(",", "")+",");
		out.write(":");
		for(String ri:right)
			if(!"".equals(ri) && !",".equals(ri))
				out.write(ri.replaceAll(",", "")+",");
		out.write("\n");
		if(left.size() == 1){
			out1.write(left.get(0).replaceAll(",", "")+",");
			out1.write(":");
			for(String ri:right)
				if(!"".equals(ri) && !",".equals(ri))
					out1.write(ri.replaceAll(",", "")+",");
			out1.write("\n");
		}
	}
	
	public static void convertFile(String filePath) throws IOException {
		File fileDir = new File(filePath);

		BufferedReader in = new BufferedReader(new InputStreamReader(new FileInputStream(fileDir), "UTF8"));
		Writer out = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(filePath+".out"), "UTF-8"));
		Writer out1 = new BufferedWriter(new OutputStreamWriter(new FileOutputStream(filePath+".single.out"), "UTF-8"));

		String line;
		List<String> lines = new ArrayList<>();
		while ((line = in.readLine()) != null) {
			line = line.trim();
			lines.add(line);
		}
		in.close();
		combineLines(lines, out, out1);
		out.close();
		out1.close();
	}

	
	public static void combineLines(List<String> lines, Writer out, Writer out1) throws IOException{
		List<String> prevLeft = new ArrayList<>();
		List<String> prevRight = new ArrayList<>();

		List<String> curLeft = new ArrayList<>();
		List<String> curRight = new ArrayList<>();

		
		boolean continued = false;

		for (String str : lines) {
			if(!str.contains("=>"))
				continue;
			curLeft = trimArray(str.split("=>")[0].split(" "));
			curRight = trimArray(str.split("=>")[1].split("\\+"));
			if ((str.endsWith("+") || str.endsWith("+,")) && !continued) {
				continued = true;
				prevLeft.addAll(curLeft);
				prevRight.addAll(curRight);
			} else if ((str.endsWith("+") || str.endsWith("+,")) && continued) {
				continued = true;
				prevLeft = mergeLists(prevLeft, curLeft);
				prevRight = mergeLists(prevRight, curRight);
			} else {
				continued = true;
				prevLeft = mergeLists(prevLeft, curLeft);
				prevRight = mergeLists(prevRight, curRight);
				writeToFile(prevLeft, prevRight, out, out1);
				prevLeft = new ArrayList<>();
				prevRight = new ArrayList<>();
			}
		}
	}
	
	private static List<String> mergeLists(List<String> prevList,
			List<String> curList) throws IOException {
		//int commonLength = getCommonLength(prevList, curList);
		int common = getCommonSize(prevList, curList);
		/*for (int i = commonLength; i > 0; i--) {
			List<String> prevTail = prevList.subList(prevList.size() - i,  prevList.size());
			List<String> curHead = curList.subList(0, i);
			if (prevTail.equals(curHead)) {
				common = i;
				break;
			}
		}*/
		for (int i = common; i < curList.size(); i++)
			prevList.add(curList.get(i));
		return prevList;

	}

	public static List<String> trimArray(String[] array) {
		List<String> arr = new ArrayList<String>();
		for (int i = 0; i < array.length; i++)
			arr.add(array[i].trim());
		return arr;

	}

	public static int max(int a, int b) {
		return (a > b) ? a : b;
	}

	public static int getCommonLength(List<String> oldList, List<String> newList) {
		int m = oldList.size();
		int n = newList.size();
		int[][] tempMatrix = new int[m + 1][n + 1];
		int result = 0;
		for (int i = 0; i <= m; i++) {
			for (int j = 0; j <= n; j++) {
				if (i == 0 || j == 0)
					tempMatrix[i][j] = 0;

				else if (oldList.get(i - 1).equals(newList.get(j - 1))) {
					tempMatrix[i][j] = tempMatrix[i - 1][j - 1] + 1;
					result = max(result, tempMatrix[i][j]);
				} else
					tempMatrix[i][j] = 0;
			}
		}
		return result;
	}
	
	public static int getCommonSize(List<String> oldList, List<String> newList) {
		int m = oldList.size();
		int n = newList.size();
		int result = 0;
		for (int i = m - 1, j = n - 1; i >= 0 && j >= 0 ; i--, j--) {
			if (oldList.get(i).equals(newList.get(j))) {
				result++;
			} else
				return result;
		}
		return result;
	}
}
