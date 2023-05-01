package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Sol_11866 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String s = br.readLine();
        String[] arr = s.split(" ");

        ArrayList<Integer> list = new ArrayList<>();
        ArrayList<Integer> result = new ArrayList<>();
        for (int i = 1; i <= Integer.parseInt(arr[0]); i++) {
            list.add(Integer.valueOf(i));
        }
        int size = list.size();
        int index = 0;
        while ((list.isEmpty()) == false) {
            for (int i = 0; i < Integer.parseInt(arr[1]) - 1; i++) {
                if (index < size - 1) {
                    index++;
                } else {
                    index = 0;
                }
            }
            result.add(list.remove(index));
            size--;
            if (index == size) {
                index = 0;
            }
        }
        String temp = "<";
        for (int i = 0; i < result.size(); i++) {
            temp += result.get(i);
            if (i < result.size()-1) {
                temp += ", ";
            }
        }
        temp += ">";
        System.out.println(temp);
    }
}
