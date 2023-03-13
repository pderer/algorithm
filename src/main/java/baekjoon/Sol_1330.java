package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_1330 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();

        String[] arr = s.split(" ");

        if (Integer.parseInt(arr[0]) > Integer.parseInt(arr[1])) {
            System.out.println(">");
        } else if (Integer.parseInt(arr[0]) < Integer.parseInt(arr[1])) {
            System.out.println("<");
        } else {
            System.out.println("==");
        }
    }
}
