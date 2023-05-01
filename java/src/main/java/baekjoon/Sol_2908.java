package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_2908 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        String arr[] = s.split(" ");

        int num1 = translate(arr[0]);
        int num2 = translate(arr[1]);

        if (num1 > num2) {
            System.out.println(num1);
        } else {
            System.out.println(num2);
        }
    }

    public static int translate(String s) {
        char first = s.charAt(0);
        char second = s.charAt(1);
        char third = s.charAt(2);
        String result = new StringBuilder().append(third).append(second).append(first).toString();
        return Integer.parseInt(result);
    }
}
