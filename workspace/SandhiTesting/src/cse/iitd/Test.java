package cse.iitd;

import java.util.ArrayList;
import java.util.List;

public class Test {

	public static void main(String[] args) {

		/*
		 * String X[] = {"a","b","c","d"}; String Y[] = {"a","t","b","c","e"};
		 * 
		 * 
		 * System.out.println("Length of Longest Common Substring is " +
		 * LCSubStr(X, Y));
		 */

		String[] strings = { "a b c x => d+ e + f + g+x+", "c x d e => g+x + h" };
		String str3 = "c d e => f + g + h";

		List<String> prevLeft = new ArrayList<>();
		List<String> prevRight = new ArrayList<>();

		List<String> curLeft = new ArrayList<>();
		List<String> curRight = new ArrayList<>();

		// str1 = str1.trim();
		// str2 = str2.trim();
		str3 = str3.trim();
		boolean continued = false;

		for (String str : strings) {
			curLeft = trimArray(str.split("=>")[0].split(" "));
			curRight = trimArray(str.split("=>")[1].split("\\+"));
			if (str.endsWith("+") && !continued) {
				continued = true;
				prevLeft.addAll(curLeft);
				prevRight.addAll(curRight);
			} else if (str.endsWith("+") && continued) {
				continued = true;
				prevLeft = mergeLists(prevLeft, curLeft);
				prevRight = mergeLists(prevRight, curRight);
			} else {
				continued = true;
				prevLeft = mergeLists(prevLeft, curLeft);
				prevRight = mergeLists(prevRight, curRight);

				prevLeft = new ArrayList<>();
				prevRight = new ArrayList<>();
			}

			//System.out.println(prevLeft.toString() + "," + prevRight.toString());
		}
	}

	private static List<String> mergeLists(List<String> prevList,
			List<String> curList) {
		System.out.println(prevList.toString() + "..." + curList.toString());
		int commonLength = getCommonLength(prevList, curList);
		System.out.println("Common substring length..."+commonLength);
		int common = 0;
		for (int i = commonLength; i > 0; i--) {
			System.out.println(i);
			List<String> prevTail = prevList.subList(prevList.size() - i,  prevList.size());
			List<String> curHead = curList.subList(0, i);
			System.out.println(prevTail.toString()+".."+curHead.toString());
			if (prevTail.equals(curHead)) {
				common = i;
				break;
			}
		}
		for (int i = common; i < curList.size(); i++)
			prevList.add(curList.get(i));
		System.out.println("Final..."+prevList.toString());
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

}
