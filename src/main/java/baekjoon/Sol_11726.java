package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_11726 {
    static Integer[] memo;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        memo = new Integer[n + 1];
        memo[1] = 1;
        if (n > 1) {
            memo[2] = 2;
        }


        System.out.println(calculate(n));
    }

    static Integer calculate(int n) {
        if (memo[n] == null) {
            memo[n] = (calculate(n - 1) + calculate(n - 2)) % 10007;
        }
        return memo[n];
    }
}
