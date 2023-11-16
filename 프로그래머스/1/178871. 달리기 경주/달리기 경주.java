import java.util.HashMap;
class Solution {
    public String[] solution(String[] players, String[] callings) {
        HashMap<String, Integer> line = new HashMap<>();
        for(int i = 0; i<players.length; i++){
            line.put(players[i],i);
        }
       for(String player : callings){
           int rank = line.get(player);
           String before = players[rank - 1];
           
           players[rank-1] = player;
           players[rank] = before;
           
           line.put(player,rank-1);
           line.put(before,rank);
       }
        return players;
    }
}