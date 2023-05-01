package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_11050 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String[] arr = s.split(" ");
        int num1 = Integer.parseInt(arr[0]);
        int num2 = Integer.parseInt(arr[1]);

        System.out.println(factorial(num1) / factorial(num2) / factorial(num1 - num2));
    }

    public static int factorial(int num) {
        int temp = 1;
        for (int i = 1; i <= num; i++) {
            temp *= i;
        }
        return temp;
    }
}
