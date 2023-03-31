package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_1003 {
    static Integer[][] memo = new Integer[41][2];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int test = Integer.parseInt(br.readLine());
        memo[0][0] = 1;
        memo[0][1] = 0;
        memo[1][0] = 0;
        memo[1][1] = 1;

        for (int i = 0; i < test; i++) {
            int temp = Integer.parseInt(br.readLine());
            fibonacci(temp);
            sb.append(memo[temp][0]).append(" ").append(memo[temp][1]).append("\n");
        }

        System.out.println(sb);
    }
    static Integer[] fibonacci(int n) {
        if (memo[n][0] == null || memo[n][1] == null) {
            memo[n][0] = fibonacci(n - 1)[0] + fibonacci(n - 2)[0];
            memo[n][1] = fibonacci(n - 1)[1] + fibonacci(n - 2)[1];
        }
        return memo[n];
    }
}
