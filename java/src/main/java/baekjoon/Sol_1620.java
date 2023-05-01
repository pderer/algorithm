package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Sol_1620 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String s = br.readLine();
        String[] commands = s.split(" ");
        int total = Integer.parseInt(commands[0]);
        int check = Integer.parseInt(commands[1]);
        HashMap<String, Integer> hashMap = new HashMap<>();
        String[] strings = new String[total];

        for (int i = 0; i < total; i++) {
            String temp = br.readLine();
            hashMap.put(temp, i + 1);
            strings[i] = temp;
        }
        for (int i = 0; i < check; i++) {
            String temp = br.readLine();
            try {
                int index = Integer.parseInt(temp);
                sb.append(strings[index - 1]).append("\n");
            } catch (NumberFormatException e) {
                int index = hashMap.get(temp);
                sb.append(index).append("\n");
            }
        }
        System.out.println(sb);
    }
}
