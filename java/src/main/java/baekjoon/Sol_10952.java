package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_10952 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String s = br.readLine();
            String[] arr = s.split(" ");
            if (arr[0].equals("0") && arr[1].equals("0")) {
                break;
            }
            int sum = Integer.parseInt(arr[0]) + Integer.parseInt(arr[1]);
            System.out.println(sum);
        }
    }
}
