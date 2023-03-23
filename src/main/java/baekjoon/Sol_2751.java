package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Sol_2751 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        Integer[] ints = new Integer[n];

        for (int i = 0; i < n; i++) {
            ints[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(ints);

        for (int i = 0; i < n; i++) {
            sb.append(ints[i]).append("\n");
        }
        System.out.println(sb);
    }
}
