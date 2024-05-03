class Solution {
    public int solution(int[] numbers, int n) {
        int answer = 0;
        int count = 0;
        while(n >= answer){
            answer += numbers[count];
            count += 1;
        }
        return answer;
    }
}