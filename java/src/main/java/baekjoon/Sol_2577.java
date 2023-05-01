package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_2577 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[] arr = new int[3];
        for (int i = 0; i < 3; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }
        int temp = arr[0] * arr[1] * arr[2];

        String s = Integer.toString(temp);

        int[] result = new int[10];

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            result[Character.getNumericValue(c)]++;
        }

        for (int i = 0; i < result.length; i++) {
            System.out.println(result[i]);
        }
    }
}
