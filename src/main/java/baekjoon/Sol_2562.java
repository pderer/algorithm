package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_2562 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int result = 0;
        int index = 0;
        for (int i = 0; i < 9; i++) {
            int temp = Integer.parseInt(br.readLine());
            if (temp > result) {
                result = temp;
                index = i+1;
            }
        }
        System.out.println(result);
        System.out.println(index);
    }
}
