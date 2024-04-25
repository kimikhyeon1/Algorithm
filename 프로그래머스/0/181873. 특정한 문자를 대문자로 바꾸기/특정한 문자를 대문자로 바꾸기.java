class Solution {
    public String solution(String my_string, String alp) {
        String answer = "";
        char alpConvert = (char)((int)alp.charAt(0) - 32) ;
        
        for (char ch : my_string.toCharArray()){
            if (ch == alp.charAt(0)){
                answer += alpConvert;
                continue;
            }
            answer += ch;
        }
        return answer;
    }
}