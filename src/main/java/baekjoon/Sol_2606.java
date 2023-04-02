package baekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;

public class Sol_2606 {
    static Node[] nodes;
    static ArrayList<LinkedList<Node>> linkedLists;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int totalNode = Integer.parseInt(br.readLine());
        int pair = Integer.parseInt(br.readLine());

        nodes = new Node[totalNode];
        linkedLists = new ArrayList<>(totalNode);

        for (int i = 0; i < totalNode; i++) {
            nodes[i] = new Node(-1, i);
            LinkedList<Node> nodelist = new LinkedList<>();
            linkedLists.add(i, nodelist);
        }

        for (int i = 0; i < pair; i++) {
            String string = br.readLine();
            String[] strings = string.split(" ");
            int temp1 = Integer.parseInt(strings[0]) - 1;
            int temp2 = Integer.parseInt(strings[1]) - 1;
            linkedLists.get(temp1).add(nodes[temp2]);
            linkedLists.get(temp2).add(nodes[temp1]);
        }
        DFS(0);

        int result = 0;
        for (Node node : nodes) {
            if (node.status == 1) {
                result++;
            }
        }
        System.out.println(result - 1);
    }

    static void DFS(int start) {
        nodes[start].status = 0; // in progress
        for (Node node : linkedLists.get(start)) {
            if (node.status == -1) {
                DFS(node.index);
            }
        }
        nodes[start].status = 1; // in progress
    }
}

class Node {
    int status; //  -1 : unvisited, 0: progress, 1 : all done
    int index;

    public Node(int status, int index) {
        this.status = status;
        this.index = index;
    }
}
