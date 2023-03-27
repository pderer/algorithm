package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class Sol_1764 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String s = br.readLine();
        String[] strings = s.split(" ");

        int n1 = Integer.parseInt(strings[0]);
        int n2 = Integer.parseInt(strings[1]);

        HashSet<String> heard = new HashSet<>();
        ArrayList<String> result = new ArrayList<>();

        for (int i = 0; i < n1; i++) {
            heard.add(br.readLine());
        }

        for (int i = 0; i < n2; i++) {
            String temp = br.readLine();
            if (heard.contains(temp)) {
                result.add(temp);
            }
        }
        Collections.sort(result);
        sb.append(result.size()).append("\n");
        for (String temp : result) {
            sb.append(temp).append("\n");
        }
        System.out.println(sb);
    }
}
