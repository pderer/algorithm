package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Sol_11399 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int[] people = new int[n];

        String s = br.readLine();
        String[] strings = s.split(" ");

        for (int i = 0; i < n; i++) {
            people[i] = Integer.parseInt(strings[i]);
        }

        Arrays.sort(people);

        int[] temp = new int[n];
        for (int i = 0; i < n; i++) {
            if (i == 0) {
                temp[i] = people[i];
            } else {
                temp[i] = temp[i - 1] + people[i];
            }
        }

        int result = 0;

        for (int i : temp) {
            result += i;
        }

        System.out.println(result);
    }
}
