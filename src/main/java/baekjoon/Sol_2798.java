package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_2798 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        String[] strings = s.split(" ");

        int num = Integer.parseInt(strings[0]);
        int blackjack = Integer.parseInt(strings[1]);

        String tempstring = br.readLine();
        String[] temps = tempstring.split(" ");
        int[] cards = new int[num];
        for (int i = 0; i < num; i++) {
            cards[i] = Integer.parseInt(temps[i]);
        }

        int result = 0;

        for (int i = 0; i < num - 2; i++) {
            for (int j = i + 1; j < num - 1; j++) {
                for (int k = j + 1; k < num; k++) {
                    int temp = cards[i] + cards[j] + cards[k];
                    if (temp == blackjack) {
                        System.out.println(temp);
                        return;
                    }
                    if (temp < blackjack && temp > result) {
                        result = temp;
                    }
                }
            }
        }
        System.out.println(result);
    }
}
