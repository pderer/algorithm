package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_2675 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            String[] arr = s.split(" ");
            for (int j = 0; j < arr[1].length(); j++) {
                for (int k = 0; k < Integer.parseInt(arr[0]); k++) {
                    sb.append(arr[1].charAt(j));
                }
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }
}
