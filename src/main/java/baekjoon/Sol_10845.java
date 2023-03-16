package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Deque;

public class Sol_10845 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());
        Deque<Integer> queue = new ArrayDeque<>();
        Integer temp;
        for (int i = 0; i < num; i++) {
            String s = br.readLine();
            String[] arr = s.split(" ");
            switch (arr[0]) {
                case "push":
                    queue.add(Integer.parseInt(arr[1]));
                    break;
                case "pop":
                    if ((temp = queue.poll()) == null) {
                        System.out.println(-1);
                    } else {
                        System.out.println(temp);
                    }
                    break;
                case "size":
                    System.out.println(queue.size());
                    break;
                case "empty":
                    if (queue.isEmpty()) {
                        System.out.println(1);
                    } else {
                        System.out.println(0);
                    }
                    break;
                case "front":
                    if ((temp = queue.peek()) == null) {
                        System.out.println(-1);
                    } else {
                        System.out.println(temp);
                    }
                    break;
                case "back":
                    if ((temp = queue.peekLast()) == null) {
                        System.out.println(-1);
                    } else {
                        System.out.println(temp);
                    }
                    break;
            }
        }
    }
}
