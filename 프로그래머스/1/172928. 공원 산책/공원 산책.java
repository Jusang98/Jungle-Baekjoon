class Solution {
    public int[] solution(String[] park, String[] routes) {
        int sx = 0;
        int sy = 0;
        
        char[][] arr = new char[park.length][park[0].length()];
        
        for(int i = 0; i < park.length; i++){
            arr[i] = park[i].toCharArray();
            
            if(park[i].contains("S")){
                sy = i;
                sx = park[i].indexOf("S");
            }
        }
    
        for(String st : routes){
            String way = st.split(" ")[0];
            int len = Integer.parseInt(st.split(" ")[1]);
            
            int nx = sx;
            int ny = sy;
            
            for(int i = 0; i < len; i++){
                if(way.equals("E")){
                    nx++;
                }
                if(way.equals("W")){
                    nx--;
                }
                if(way.equals("S")){
                    ny++;
                }
                if(way.equals("N")){
                    ny--;
                }
                if(nx >=0 && ny >=0 && ny < arr.length && nx < arr[0].length){
                    if(arr[ny][nx] == 'X'){
                        break;
                    }
                    // 범위내 & 장애물 x
                    if(i == len-1){
                        sx = nx;
                        sy = ny;
                    }
                }
            }
        }       
        
        int[] answer = {sy, sx};
        return answer;
    }
}
