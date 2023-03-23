package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Sol_10816 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        String s = br.readLine();
        String[] strings = s.split(" ");
        HashMap<String, Integer> hashMap = new HashMap<>();

        for (int i = 0; i < n; i++) {
            if (hashMap.containsKey(strings[i])) {
                Integer temp = hashMap.get(strings[i]);
                hashMap.replace(strings[i], ++temp);
            } else {
                hashMap.put(strings[i], 1);
            }
        }

        int n2 = Integer.parseInt(br.readLine());
        String s2 = br.readLine();
        String[] strings2 = s2.split(" ");
        for (int i = 0; i < n2; i++) {
            if (hashMap.containsKey(strings2[i])) {
                sb.append(hashMap.get(strings2[i])).append(" ");
            } else {
                sb.append("0 ");
            }
        }

        System.out.println(sb);
    }
}
