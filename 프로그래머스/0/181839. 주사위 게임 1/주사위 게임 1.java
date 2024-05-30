class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        if (a % 2 == 1 && b % 2 == 1){
            return a*a + b*b;
        }
        if (a % 2 == 1 || b % 2 == 1){
            return 2 * (a + b);
        }
        return a - b < 0 ? -1 * (a - b) : a - b;
    }
}