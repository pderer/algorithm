package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_1463 {
    static Integer[] memo;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        memo = new Integer[n + 1];
        memo[0] = 0;
        memo[1] = 0;
        System.out.println(dynamic(n));
    }
    static int dynamic(int n) {
        if (memo[n] == null) {
            if (n % 6 == 0) {
                memo[n] = Math.min(Math.min(dynamic(n / 3), dynamic(n / 2)), dynamic(n - 1)) + 1;
            } else if (n % 3 == 0) {
                memo[n] = Math.min(dynamic(n - 1), dynamic(n / 3)) + 1;
            } else if (n % 2 == 0) {
                memo[n] = Math.min(dynamic(n - 1), dynamic(n / 2)) + 1;
            } else {
                memo[n] = dynamic(n - 1) + 1;
            }
        }
        return memo[n];
    }
}
