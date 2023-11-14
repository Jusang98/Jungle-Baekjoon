class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String stra = String.valueOf(a);
        String strb = String.valueOf(b);
        String strab = stra+strb;
        int ab = Integer.valueOf(strab);
        int ab2 = 2 * a * b;
        
        if(ab >= ab2){
            answer += ab;
        }else{
            answer += ab2;
        }
        
        return answer;
    }
}