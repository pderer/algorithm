package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;

public class Sol_10814 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        Member[] members = new Member[n];

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            String[] arr = s.split(" ");
            members[i] = new Member(Integer.parseInt(arr[0]), arr[1]);
        }

        Comparator<Member> comparator = (o1, o2) -> {
            if (o1.age > o2.age) {
                return 1;
            } else if (o1.age == o2.age) {
                if (o1.memberNumber > o2.memberNumber) {
                    return 1;
                }
                return 0;
            }
            return -1;
        };

        Arrays.sort(members, comparator);

        for (int i = 0; i < n; i++) {
            sb.append(members[i].age).append(" ").append(members[i].name).append("\n");
        }
        System.out.println(sb);
    }
}

class Member {
    static int nextMemberNumber = 0;
    int memberNumber;
    int age;
    String name;

    public Member(int age, String name) {
        memberNumber = nextMemberNumber;
        nextMemberNumber++;
        this.age = age;
        this.name = name;
    }
}
