import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_2110_공유기설치 {

    static int[] house;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken()); // 집 개수
        int C = Integer.parseInt(st.nextToken()); // 공유기 개수

        house = new int[N];
        for (int i = 0; i < N; i++) {
            house[i] = Integer.parseInt(br.readLine()); // 집 위치
        }
        Arrays.sort(house); // 오름차순 정렬

        int left = 1; // 공유기 간 거리 최소값
        int right = house[N-1] - house[0] + 1; // 공유기 간 거리 최대값

        while(left<right){
            int mid = (left+right)/2; // 중간값

            // 설치가능한 공유기 개수
            int cnt = install(mid);

            if(cnt<C){ // 공유기 간 거리를 줄여야함
                right = mid;
            }else{ // 공유기 간 거리 늘려야함
                left = mid+1;
            }
        }

        System.out.println(left-1); // while문이 값이 초과됐을때 빠져나오므로 -1 해줘야함
    }

    private static int install(int mid) {

        int cnt = 1; // 처음 집은 무조건 설치
        int prev = house[0]; // 직전에 설치했던 집 위치

        for (int i = 1; i < house.length; i++) {
            int loc = house[i];

            // 다음 집 위치랑 이전에 공유기 설치했던 집 위치가
            // mid보다 크거나 같으면 공유기 설치 가능
            if(loc-prev>=mid){
                cnt++;
                prev = loc;
            }
        }

        return cnt;
    }
}

