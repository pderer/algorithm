package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_2920 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        String arr[] = s.split(" ");

        if (arr[0].equals("1")) {
            for (int i = 0; i < 7; i++) {
                if (Integer.parseInt(arr[i]) != (i + 1)) {
                    System.out.println("mixed");
                    return;
                }
            }
            System.out.println("ascending");
            return;
        }
        if (arr[0].equals("8")) {
            for (int i = 0; i < 7; i++) {
                if (Integer.parseInt(arr[i]) != (8 - i)) {
                    System.out.println("mixed");
                    return;
                }
            }
            System.out.println("descending");
            return;
        }
        System.out.println("mixed");
    }
}
