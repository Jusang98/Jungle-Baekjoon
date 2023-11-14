class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String stra = String.valueOf(a);
        String strb = String.valueOf(b);
        String ab = stra + strb;
        String ba = strb + stra;
        int intab = Integer.valueOf(ab);
        int intba = Integer.valueOf(ba);
        if(intab> intba){
            answer += intab;
        }else{
            answer += intba;
        }
        
        return answer;
    }
}