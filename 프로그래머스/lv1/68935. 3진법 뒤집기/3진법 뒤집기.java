class Solution {
    public int solution(int n) {
                int answer = 0;
        int moc = n;
        int i =0;
        int[] array = new int[100];
        while(moc>0){
            array[i] = moc%3;
            moc /=3;
            i++;
        }
        i--;
        int count = 0;
        for (; i >=0 ; i--) {
            answer += array[i]*Math.pow(3,count);
            count++;
        }
        return answer;
    }
}