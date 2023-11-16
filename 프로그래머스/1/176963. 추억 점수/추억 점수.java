import java.util.HashMap;
class Solution {
    public int[] solution(String[] name, int[] yearning, String[][] photo) {
        HashMap<String, Integer> map = new HashMap<>();
        for(int i = 0; i< name.length; i++){
            map.put(name[i],yearning[i]);
        }
        
    
        int[] answer = new int[photo.length];
        for(int i = 0; i < photo.length; i++){
            int score = 0;
            String [] persons = photo[i];
            for(int j = 0; j< persons.length;j++){
                if(map.containsKey(persons[j])){
                    score += map.get(persons[j]);
                }
            }
            answer [i] = score;
        }
        return answer;
    }
}