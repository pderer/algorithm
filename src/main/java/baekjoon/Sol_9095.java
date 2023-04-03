package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_9095 {
    static Integer[] memo = new Integer[11];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        memo[1] = 1;
        memo[2] = 2;
        memo[3] = 4;

        for (int i = 0; i < n; i++) {
            sb.append(numberOfCases(Integer.parseInt(br.readLine()))).append("\n");
        }
        System.out.println(sb);
    }

    static int numberOfCases(int n) {
        if (memo[n] == null) {
            memo[n] = numberOfCases(n - 1) + numberOfCases(n - 2) + numberOfCases(n - 3);
        }
        return memo[n];
    }
}
