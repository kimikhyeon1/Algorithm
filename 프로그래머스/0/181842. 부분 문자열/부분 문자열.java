class Solution {
    public int solution(String str1, String str2) {
        int answer = 0;
        int start = 0;
        for (int end = str1.length(); end <= str2.length(); end++){
            if (str2.substring(start,end).equals(str1)){
                return 1;
            }
            start += 1;
        }
        return answer;
    }
}