package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Sol_1920 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        HashSet<Integer> hashSet = new HashSet<>();
        String s = br.readLine();
        String[] arr = s.split(" ");

        for (int i = 0; i < n; i++) {
            hashSet.add(Integer.parseInt(arr[i]));
        }

        int check = Integer.parseInt(br.readLine());
        String temp = br.readLine();
        String[] strings = temp.split(" ");

        for (int i = 0; i < check; i++) {
            if (hashSet.contains(Integer.parseInt(strings[i]))) {
                sb.append(1).append("\n");
            } else {
                sb.append(0).append("\n");
            }
        }

        System.out.println(sb);

    }
}
