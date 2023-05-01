package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Sol_4153 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String s = br.readLine();
            String[] arr = s.split(" ");
            if (arr[0].equals("0") && arr[1].equals("0") && arr[2].equals("0")) {
                break;
            }
            ArrayList<Integer> arrayList = new ArrayList<>();
            for (int i = 0; i < 3; i++) {
                arrayList.add(Integer.parseInt(arr[i]));
            }
            Integer max = arrayList.get(0);
            int maxIndex = 0;
            for (int i = 1; i < 3; i++) {
                if (arrayList.get(i) > max) {
                    max = arrayList.get(i);
                    maxIndex = i;
                }
            }
            Integer temp = arrayList.remove(maxIndex);
            if (Math.pow(temp, 2) == (Math.pow(arrayList.get(0), 2) + Math.pow(arrayList.get(1), 2))) {
                System.out.println("right");
            } else {
                System.out.println("wrong");
            }
        }
    }
}
