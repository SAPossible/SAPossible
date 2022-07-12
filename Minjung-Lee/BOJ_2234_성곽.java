import java.awt.*;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.List;

public class BOJ_2234_성곽 {

    static int[] dx = {1,0,-1,0};
    static int[] dy = {0,1,0,-1};
    static int N, M, maxRoomSize;
    static int[][][] map;
    static int[][] visited;
    static List<Integer> roomSize;
    static List<List<Integer>> nearRoom; // 인접방

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        map = new int[M][N][4];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < N; j++) {
                String[] wall = Integer.toBinaryString(Integer.parseInt(st.nextToken())).split(""); // 이진법으로 바꿈
                for(int k = 0; k<wall.length; k++){
                    map[i][j][k+4-wall.length] = Integer.parseInt(wall[k]);
                }
            }
        }

        visited = new int[M][N];
        nearRoom = new LinkedList<>();
        roomSize = new LinkedList<>();
        maxRoomSize = 0;
        int roomNum = 1;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                if(visited[i][j]==0){
                    check(i,j, roomNum);
                    roomNum++; // 방번호 증가
                }
            }
        }

        System.out.println(roomSize.size());
        System.out.println(maxRoomSize);

        // 방 합쳤을때
        int addRoom = 0;
        for (int i = 0; i < nearRoom.size(); i++) {
            for (int j = 0; j < nearRoom.get(i).size(); j++) {
                addRoom = Math.max(addRoom,roomSize.get(i)+roomSize.get(nearRoom.get(i).get(j)-1));
            }
        }
        System.out.println(addRoom);
    }

    private static void check(int i, int j, int roomNum) {
        int size = 1;
        Queue<Point> q = new LinkedList<>();
        q.add(new Point(i,j));
        visited[i][j] = roomNum;

        List<Integer> near = new LinkedList<>();
        while(!q.isEmpty()){
            Point cur = q.poll();
            for (int d = 0; d < 4; d++) {
                int nx = cur.x + dx[d];
                int ny = cur.y + dy[d];

                if(map[cur.x][cur.y][d]==0 && visited[nx][ny]==0){ // 벽이 아니고 방문 안했으면 ㄱ
                    size++;
                    q.add(new Point(nx,ny));
                    visited[nx][ny] = roomNum;
                }else if(map[cur.x][cur.y][d]==1){
                    if(nx>=0 && nx<M && ny>=0 && ny<N && visited[nx][ny]!=0 && visited[nx][ny]!=roomNum){
                        if(!near.contains(visited[nx][ny]))
                            near.add(visited[nx][ny]); // 인접방
                    }
                }
            }
        }
        nearRoom.add(near);
        roomSize.add(size);
        maxRoomSize = Math.max(maxRoomSize, size);
    }
}

