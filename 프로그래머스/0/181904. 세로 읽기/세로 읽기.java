class Solution {
    public String solution(String my_string, int m, int c) {
        c = c - 1;
        String answer = "";
        for (int i = 0; i < my_string.length(); i++){
            if (my_string.length() <= c){
                break;
            }
            answer += my_string.charAt(c);
            c = c + m;
        }
        return answer;
    }
}