import java.util.*;
class Solution {
    static int[] answer;
    static HashMap<String, Integer> map;
    
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {
        answer = new int[enroll.length];
        map = new HashMap<>();

        for(int i = 0; i< enroll.length; i++){
            map.put(enroll[i],i);
        }

        for (int i = 0; i < seller.length ; i++) {
            int idx = map.get(seller[i]);
            int money = amount[i]*100;
            answer[idx] += (int)(money*0.9);
            if(!referral[idx].equals("-")){
                divide(referral, referral[idx], map.get(referral[idx]), (int)(money*0.1));
            }
            
        }

       return answer;
    }

    private static void divide(String[] referral, String name, int idx, int money) {
        int ten = (int)(money*0.1); // 10%
        answer[idx] += money-ten;
        if(referral[idx].equals("-") || ten<1){
            return;
        }
        divide(referral, referral[idx], map.get(referral[idx]), ten);
    }
}
