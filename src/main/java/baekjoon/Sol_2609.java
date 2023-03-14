package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_2609 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String[] arr = s.split(" ");
        int num1 = Integer.parseInt(arr[0]);
        int num2 = Integer.parseInt(arr[1]);

        int min = (num1 < num2 ? num1 : num2);
        int gcd = 0;
        int lcm = 0;

        for (int i = min; i > 0; i--) {
            if (num1 % i == 0 && num2 % i == 0) {
                gcd = i;
                break;
            }
        }

        lcm = num1 * num2 / gcd;

        System.out.println(gcd);
        System.out.println(lcm);

    }
}
