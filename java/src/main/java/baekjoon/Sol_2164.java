package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Queue;

public class Sol_2164 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());
        if (num == 1) {
            System.out.println(1);
            return;
        }
        Queue<Integer> queue = new ArrayDeque<>();

        for (int i = 1; i <= num; i++) {
            queue.add(Integer.valueOf(i));
        }

        while (true) {
            queue.poll();
            if (queue.size() == 1) {
                break;
            }
            queue.add(queue.poll());
        }
        System.out.println(queue.peek());
    }
}
