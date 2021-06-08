package june04;

import java.util.Scanner;

public class Test02 {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		Solution mini = new Solution();
		System.out.println("암호화할 문자열을 입력해주세요.");
		String input = sc.next();
		System.out.println(mini.solution(input));

	}
}

class Solution {
	int number = 2;
	int number2 = 2;

	public String solution(String input) {
		String answer = "";

		for (int i = 0; i < input.length(); i++) {
			char ch = input.charAt(i);

			if (i % 2 == 0) {
				ch = (char) ((ch - 'a' + number) % 26 + 'a');
				number++;
			} else {
				ch = (char) ((ch - 'a' - number2) * (-25) + 'a');
				number2++;
			}
			answer += ch;
		}

		return answer;
	}
}