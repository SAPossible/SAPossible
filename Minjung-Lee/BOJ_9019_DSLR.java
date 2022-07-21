import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_9019_DSLR {

    static class Value{
        int number;
        String order;

        public Value(int number, String order) {
            this.number = number;
            this.order = order;
        }
    }

    static StringBuilder sb;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        sb = new StringBuilder();
        StringTokenizer st = null;
        for (int i = 0; i < T; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            bfs(A,B);
        }

        System.out.println(sb);
    }

    private static void bfs(int A, int B) {
        boolean[] visited = new boolean[10000];

        Queue<Value> q = new LinkedList<>();
        q.add(new Value(A,""));
        visited[A] = true;

        while (!q.isEmpty()){
            Value cur = q.poll();

            if(cur.number==B){
                sb.append(cur.order).append("\n");
                return;
            }

            //D
            int newNum = (cur.number*2)%10000;
            if(!visited[newNum]){
                q.add(new Value(newNum, cur.order + "D"));
                visited[newNum] = true;
            }

            //S
            newNum = (cur.number-1)<0?9999:cur.number-1;
            if(!visited[newNum]){
                q.add(new Value(newNum, cur.order + "S"));
                visited[newNum] = true;
            }

            //L
            newNum = (cur.number * 10) % 10000 + (cur.number/1000);
            if(!visited[newNum]){
                q.add(new Value(newNum, cur.order + "L"));
                visited[newNum] = true;
            }

            //R
            newNum = (cur.number / 10) + (cur.number % 10) * 1000;
            if(!visited[newNum]){
                q.add(new Value(newNum, cur.order + "R"));
                visited[newNum] = true;
            }
        }
    }
}

