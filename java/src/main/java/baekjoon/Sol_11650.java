package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Sol_11650 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int num = Integer.parseInt(br.readLine());

        int[][] array = new int[num][2];

        for (int i = 0; i < num; i++) {
            String s = br.readLine();
            String[] strings = s.split(" ");
            for (int j = 0; j < 2; j++) {
                array[i][j] = Integer.parseInt(strings[j]);
            }
        }

        Comparator<int[]> comparator = (o1, o2) -> {
            if (o1[0] > o2[0]) {
                return 1;
            } else if (o1[0] == o2[0]) {
                if (o1[1] > o2[1]){
                    return 1;
                }
            }
            return -1;
        };
        Arrays.sort(array, comparator);

        for (int i = 0; i < num; i++) {
            sb.append(array[i][0]).append(" ").append(array[i][1]).append("\n");
        }
        System.out.println(sb);
    }
}
