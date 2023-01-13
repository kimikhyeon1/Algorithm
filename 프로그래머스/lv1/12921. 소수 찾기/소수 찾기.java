class Solution {
    public int solution(int n) {
        int answer = 0;
        int[] array = new int[n+1];
        for (int i = 2; i <=n ; i++) {
            array[i]=i;
        }
        for (int i = 2; i*i <=n ; i++) {
            if (array[i]==0)continue;
            for (int j = i*i; j <=n ; j+=i) {
                array[j]=0;
            }
        }
        for (int i = 0; i <= n ; i++) {
            if (array[i]>0){
                answer+=1;
            }
        }
        return answer;
    }
}