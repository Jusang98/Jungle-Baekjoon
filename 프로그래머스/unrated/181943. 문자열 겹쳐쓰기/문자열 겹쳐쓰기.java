class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer ="";
        for(int i = 0; i<s; i++){
            answer += my_string.charAt(i);
        }
        String result = answer+overwrite_string;
        if(my_string.length()>(result).length()){
            result += my_string.substring(result.length());
        }
        return result;
    }
    
}