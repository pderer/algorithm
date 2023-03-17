package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_1978 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int num = Integer.parseInt(br.readLine());
        String s = br.readLine();
        String[] arr = s.split(" ");
        int count = 0;

        for (int i = 0; i < num; i++) {
            int temp = Integer.parseInt(arr[i]);
            if (temp == 1) {
                count++;
                continue;
            }
            for (int j = 2; j < temp; j++) {
                if (temp % j == 0) {
                    count++;
                    break;
                }
            }
        }
        System.out.println(num-count);
    }
}
