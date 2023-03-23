package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_10250 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            String[] strings = s.split(" ");
            int height = Integer.parseInt(strings[0]);
            int weight = Integer.parseInt(strings[1]);
            int order = Integer.parseInt(strings[2]);

            System.out.println(calculateRoom(height, weight, order));
        }
    }

    public static String calculateRoom(int height, int weight, int order) {
        int count = 0;
        int roomHeight;
        int roomWeight;
        String result;
        for (int i = 1; i <= weight; i++) {
            for (int j = 1; j <= height; j++) {
                roomHeight = j;
                roomWeight = i;
                count++;
                if (count == order) {
                    result = Integer.toString(roomHeight);
                    if (roomWeight < 10) {
                        result = result + "0" + roomWeight;
                    } else {
                        result += Integer.toString(roomWeight);
                    }
                    return result;
                }
            }
        }
        return "error";
    }
}
