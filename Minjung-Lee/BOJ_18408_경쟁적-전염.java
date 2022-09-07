import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ_18408_경쟁적전염 {

    static int N,K;
    static int[][] map, copyMap;
    static int[] dx = {0,0,-1,1};
    static int[] dy = {1,-1,0,0};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken()); // NxN 시험관
        K = Integer.parseInt(st.nextToken()); // K번까지 바이러스 있음
        
        map = new int[N][N]; // 시험관
        for (int i = 0; i < N; i++) { // 초기값 넣기
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 시험관 복사 map 만들어줌
        copyMap = new int[N][N];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                copyMap[i][j] = map[i][j];
            }
        }

        boolean[][] visited = new boolean[N][N]; // 중복 방문 방지

        st = new StringTokenizer(br.readLine());
        int S = Integer.parseInt(st.nextToken()); // S초 후
        int X = Integer.parseInt(st.nextToken())-1; // 찾을 위치 X
        int Y = Integer.parseInt(st.nextToken())-1; // 찾을 위치 Y

        for (int i = 0; i < S; i++) { // S초 동안
            // map 돌면서
            for (int j = 0; j < N; j++) {
                for (int k = 0; k < N; k++) {
                    if(map[j][k]==0){ // 바이러스가 안 퍼진곳을 확인
                        virus(j,k);
                    }
                }
            }
            mapCopy(); // map에다가 copyMap을 복사함
        }

        System.out.println(map[X][Y]);
    }

    private static void mapCopy() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                map[i][j] = copyMap[i][j];
            }
        }
    }

    private static void virus(int x, int y) {
        int num = K+1; // 최대 바이러스값+1
        for (int d = 0; d < 4; d++) { // 안 퍼진 곳 기준 상하좌우 살피면서
            int nx = x + dx[d];
            int ny = y + dy[d];

            if(nx>=0 && nx<N && ny>=0 && ny<N && map[nx][ny]>0){
                num = Math.min(map[nx][ny], num); // 최소의 바이러스 번호 찾음
            }
        }

        // num==K+1은 바이러스가 없는 경우 0 그대로
        // num!=K+1이면 바이러스가 있는 거니깐 num 값 넣어주기
        if(num!=K+1){
            copyMap[x][y] = num;
        }
    }
}

