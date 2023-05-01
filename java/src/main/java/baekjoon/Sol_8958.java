package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_8958 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            int temp = 0;
            int consecutive = 0;
            for (int j = 0; j < s.length(); j++) {
                if (s.charAt(j) == 'O' && consecutive > 0) {
                    consecutive++;
                    temp += consecutive;
                }
                if (s.charAt(j) == 'O' && consecutive == 0) {
                    temp++;
                    consecutive++;
                }
                if (s.charAt(j) == 'X') {
                    consecutive = 0;
                }
            }
            System.out.println(temp);
        }
    }
}
