package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Sol_11723 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        HashSet<Integer> hashSet = new HashSet<>();

        for (int i = 0; i < n; i++) {
            String temp = br.readLine();
            String[] strings = temp.split(" ");

            switch (strings[0]) {
                case "add":
                    hashSet.add(Integer.parseInt(strings[1]));
                    break;
                case "remove":
                    hashSet.remove(Integer.parseInt(strings[1]));
                    break;
                case "check":
                    if (hashSet.contains(Integer.parseInt(strings[1]))) {
                        sb.append(1).append("\n");
                    } else {
                        sb.append(0).append("\n");
                    }
                    break;
                case "toggle":
                    if (hashSet.contains(Integer.parseInt(strings[1]))) {
                        hashSet.remove(Integer.parseInt(strings[1]));
                    } else {
                        hashSet.add(Integer.parseInt(strings[1]));
                    }
                    break;
                case "all":
                    hashSet.clear();
                    for (int j = 1; j <= 20; j++) {
                        hashSet.add(j);
                    }
                    break;
                case "empty":
                    hashSet.clear();
                    break;
            }
        }
        System.out.println(sb);
    }
}
