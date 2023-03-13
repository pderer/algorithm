package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_10818 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        String s = br.readLine();
        String[] arr = s.split(" ");

        int max = Integer.parseInt(arr[0]);
        int min = Integer.parseInt(arr[0]);

        for (int i = 0; i < n; i++) {
            if (Integer.parseInt(arr[i]) > max) {
                max = Integer.parseInt(arr[i]);
            }
            if (Integer.parseInt(arr[i]) < min) {
                min = Integer.parseInt(arr[i]);
            }
        }

        System.out.printf("%d %d", min, max);
    }
}
