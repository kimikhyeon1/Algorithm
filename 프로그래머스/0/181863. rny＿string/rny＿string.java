class Solution {
    public String solution(String rny_string) {
        String answer = "";
        for (char a : rny_string.toCharArray()){
            if (a == 'm'){
                answer += "rn";
            } else{
                answer += a;
            }
        }
        return answer;
    }
}