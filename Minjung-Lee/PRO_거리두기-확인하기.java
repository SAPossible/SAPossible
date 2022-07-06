import java.util.*;
import java.awt.Point;

class Solution {
    public int[] solution(String[][] places) {
        int answer[] = new int[5];
        
        // 대기실 5개
        for(int i = 0; i<5; i++){
            char[][] room = new char[5][5]; // 대기실
            for(int j = 0; j<5; j++){
                room[j] = places[i][j].toCharArray();
            }
            
            List<Point> waiting = new LinkedList<>(); // 대기자 리스트 
            for(int r = 0; r<5; r++){
                for(int c = 0; c<5; c++){
                    if(room[r][c]=='P'){
                        waiting.add(new Point(r,c)); // 대기자 추가 
                    }
                }
            }
            
             boolean keepDist = true;
            if(waiting.size()>1){ // 대기자가 2명 이상인 경우만 검사
                // 한명씩 비교
                check : for(int j = 0; j<waiting.size(); j++){
                    for(int k = j; k<waiting.size(); k++){
                        Point p1 = waiting.get(j);
                        Point p2 = waiting.get(k);
                        // 둘 사이의 거리 계산
                        int dist = Math.abs(p1.x - p2.x) + Math.abs(p1.y - p2.y);

                        if(dist==1){  // 거리가 1이면 바로 안됨
                            keepDist = false;
                            break check;
                        }
                        else if(dist==2){  // 거리가 2이면 확인

                            if(p2.x==p1.x-2 || p2.x==p1.x+2 || p2.y==p1.y-2 || p2.y==p1.y+2){ // 둘 사이가 직선이면
                                if(room[(p1.x+p2.x)/2][(p1.y+p2.y)/2]=='O'){ // 둘 사이에 있는게 빈 테이블이면 안됨
                                    keepDist = false;
                                    break check;
                                }
                            }
                            else{ // 둘 사이가 대각선이면
                                if(room[p1.x][p2.y]=='O' || room[p2.x][p1.y]=='O'){ // 둘 사이에 빈 테이블이 하나라도 있으면 안됨
                                    keepDist = false;
                                    break check;
                                }
                            }
                        }
                    }
                }
            }
            
            if(keepDist){
                answer[i] = 1;
            }else{
                answer[i] = 0;
            }
        }
        
        
        return answer;
    }
}
