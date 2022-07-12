import java.util.*;
class Solution {
    public long solution(int n, int[] times) {
        long answer = 0;
        Arrays.sort(times); // 시간 오름차순 정렬
        long left = 0; 
        long right =  (long) n * times[times.length-1];
        
        while(left<=right){
            long mid = (left + right) / 2;
            long cnt = 0;
            
            for(int i = 0; i<times.length; i++){
                cnt += mid / times[i];
            }
            
            if(cnt<n){ // 심사 다 못한 경우
                left = mid + 1; // 시간 더 필요
            }else{ // 심사 다 하고도 남은 경우
                right = mid - 1; // 시간 줄이기
                answer = mid;
            }
        }
        
        return answer;
    }
}
