class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        long range = x;
        for (int i=0; i<n;i++){
            answer[i] += range;
            range +=x;
        }
        return answer;
    }
}