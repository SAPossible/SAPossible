import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class BOJ_10836_여왕벌 {

    static int[][] worm;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken()); // 격자 수
        int N = Integer.parseInt(st.nextToken()); // 날짜 수

        worm = new int[M][M]; // 최초 애벌레 -> 전체 다 1
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < M; j++) {
                worm[i][j] = 1;
            }
        }

        // 왼쪽 애벌레, 위쪽 애벌레 성장하는 정도
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            int zero = Integer.parseInt(st.nextToken()); // 0개수
            int one = Integer.parseInt(st.nextToken()); // 1개수
            int two = Integer.parseInt(st.nextToken()); // 2개수

            // 왼쪽 밑부터 올라가서 위에 가면 오른쪽으로
            int idx = 0;
            for (int j = M-1; j >= 0; j--) { // 왼쪽 밑에서부터 위로
                if(zero>0){
                    worm[j][0] += 0;
                    zero--;
                }else if(one>0){
                    worm[j][0] += 1;
                    one--;
                }else if(two>0){
                    worm[j][0] += 2;
                    two--;
                }
            }
            for (int j = 1; j < M ; j++) { // 위쪽 왼쪽에서부터 오른쪽으로
                if(zero>0){
                    worm[0][j] += 0;
                    zero--;
                }else if(one>0){
                    worm[0][j] += 1;
                    one--;
                }else if(two>0){
                    worm[0][j] += 2;
                    two--;
                }
            }
        }

        // 나머지 애벌레
        for (int i = 1; i < M; i++) {
            for (int j = 1; j < M; j++) {
                worm[i][j] = compare(i,j);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < M; j++) {
                sb.append(worm[i][j]).append(" ");
            }
            sb.append("\n");
        }
        System.out.println(sb);
    }

    static int[] dx = {0,-1,-1};
    static int[] dy = {-1,-1,0};
    private static int compare(int x, int y) {
        int max = 0;
        for (int d = 0; d < 3; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];
            max = Math.max(max, worm[nx][ny]);
        }
        return max;
    }
}

