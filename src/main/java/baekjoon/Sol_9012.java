package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Sol_9012 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());

        for (int i = 0; i < num; i++) {
            String s = br.readLine();
            Stack<String> stack = new Stack<>();
            for (int j = 0; j < s.length(); j++) {
                if (s.charAt(j) == ')') {
                    if (!stack.isEmpty() && "(".equals(stack.peek())) {
                        stack.pop();
                        continue;
                    }
                    stack.push(")");
                }
                if (s.charAt(j) == '(') {
                    stack.push("(");
                }
            }
            if (stack.isEmpty()) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
