import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_16928_뱀과사다리게임 {

    static class Square{
        char c; // 사다리면 'L' 뱀이면 'S' 없으면 'N'
        int num; // 사다리거나 뱀일때 이동할 칸 번호

        public Square(char c, int num) {
            this.c = c;
            this.num = num;
        }
    }

    static class Loc{
        int num, cnt;

        public Loc(int num, int cnt) {
            this.num = num;
            this.cnt = cnt;
        }
    }

    static HashMap<Integer, Square> board;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken()); // 사다리 수
        int M = Integer.parseInt(st.nextToken()); // 뱀의 수

        // 보드판 1~100
        board = new HashMap<>();
        int n = 1;
        for (int i = 0; i < 10; i++) {
            for (int j = 0; j < 10; j++) {
                board.put(n++,new Square('N',0));
            }
        }

        // 사다리
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            board.get(x).c = 'L';
            board.get(x).num = y;
        }

        // 뱀
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());

            board.get(u).c = 'S';
            board.get(u).num = v;
        }

        System.out.println(move());
    }

    private static int move() {
        boolean[] visited = new boolean[101];
        Queue<Loc> q = new LinkedList<>();
        q.add(new Loc(1,0));
        visited[1] = true;

        while(!q.isEmpty()){
            Loc cur = q.poll();

            if(cur.num==100){
                return cur.cnt;
            }

            for (int i = 1; i <= 6; i++) {
                int nl = cur.num+i; // 이동할 위치
                if(nl<=100 && !visited[nl]){
                    if(board.get(nl).c=='L' || board.get(nl).c=='S'){
                        nl = board.get(nl).num;
                    }
                    q.offer(new Loc(nl, cur.cnt+1));
                    visited[nl] = true;
                }
            }
        }

        return 0;
    }
}

