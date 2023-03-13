package baekjoon;

import java.io.*;

public class Sol_1000 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        String arr[] = s.split(" ");

        System.out.println(Integer.parseInt(arr[0]) + Integer.parseInt(arr[1]));
    }
}
