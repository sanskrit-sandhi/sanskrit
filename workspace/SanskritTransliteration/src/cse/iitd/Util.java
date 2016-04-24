package cse.iitd;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Util {
	public static Map<String, String> getMap(String propFile) throws IOException {
		String line;
		Map<String, String> propMap = new HashMap<>();
		BufferedReader br = new BufferedReader(new FileReader(propFile));
		while ((line = br.readLine()) != null) {
			if(!line.startsWith("#")){
				String[] li = line.trim().split("=");
				propMap.put(li[0], li[1]);
			}
		}
		br.close();
		return propMap;
	}
}
