package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Sol_1018 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        String[] arr = s.split(" ");

        int row = Integer.parseInt(arr[0]);
        int column = Integer.parseInt(arr[1]);
        int count1 = 0;
        int count2 = 0;
        int min1 = 100;
        int min2 = 100;
        int result = 0;

        char[][] board = new char[row][column];

        for (int i = 0; i < row; i++) {
            String temp = br.readLine();
            for (int j = 0; j < column; j++) {
                board[i][j] = temp.charAt(j);
            }
        }

        char[][] chess1 = new char[][] {
                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'}
        };

        char[][] chess2 = new char[][] {
                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'}
        };

        for (int i = 0; i < row - 7; i++) {
            for (int j = 0; j < column - 7; j++) {
                for (int k = 0; k < 8; k++) {
                    for (int h = 0; h < 8; h++) {
                        if (board[i + k][j + h] != chess1[k][h]) {
                            count1++;
                        }
                        if (board[i + k][j + h] != chess2[k][h]) {
                            count2++;
                        }
                    }
                }
                if (count1 < min1) {
                    min1 = count1;
                }
                if (count2 < min2) {
                    min2 = count2;
                }
                count1 = 0;
                count2 = 0;
            }
        }
        result = (min1 > min2 ? min2 : min1);
        System.out.println(result);
    }
}
