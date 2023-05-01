package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Sol_10866 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());
        Deque<Integer> deque = new ArrayDeque<>();
        Integer temp = Integer.valueOf(0);

        for (int i = 0; i < num; i++) {
            String s = br.readLine();
            String[] arr = s.split(" ");

            if (arr[0].equals("push_front")) {
                deque.addFirst(Integer.parseInt(arr[1]));
            }
            if (arr[0].equals("push_back")) {
                deque.addLast(Integer.parseInt(arr[1]));
            }
            if (arr[0].equals("pop_front")) {
                if ((temp = deque.pollFirst()) == null) {
                    System.out.println(-1);
                } else {
                    System.out.println(temp);
                }
            }
            if (arr[0].equals("pop_back")) {
                if ((temp = deque.pollLast()) == null) {
                    System.out.println(-1);
                } else {
                    System.out.println(temp);
                }
            }
            if (arr[0].equals("size")) {
                System.out.println(deque.size());
            }
            if (arr[0].equals("empty")) {
                if (deque.size() == 0) {
                    System.out.println(1);
                } else {
                    System.out.println(0);
                }
            }
            if (arr[0].equals("front")) {
                if (deque.peekFirst() == null) {
                    System.out.println(-1);
                } else {
                    System.out.println(deque.peekFirst());
                }
            }
            if (arr[0].equals("back")) {
                if (deque.peekLast() == null) {
                    System.out.println(-1);
                } else {
                    System.out.println(deque.peekLast());
                }
            }
        }
    }
}
