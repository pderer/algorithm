package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_1259 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = "";

        boolean sym = true;

        while (((s = br.readLine()).equals("0")) == false) {
            for (int i = 0; i < s.length()/2; i++) {
                if (s.charAt(i) != s.charAt(s.length() - 1 - i)) {
                    sym = false;
                    break;
                }
            }
            if (sym) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }
            sym = true;
        }
    }
}
