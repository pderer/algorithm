package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_2475 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        String arr[] = s.split(" ");

        System.out.println(compute(arr));
    }

    public static int compute(String[] arr) {
        double result = 0;
        for (String value : arr) {
            result += Math.pow(Double.parseDouble(value), 2);
        }
        return (int) result % 10;
    }
}
