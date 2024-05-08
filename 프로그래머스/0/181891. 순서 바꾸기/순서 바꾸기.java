class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] answer = new int[num_list.length];
        if (num_list.length == 1){
            return num_list;
        }
        
        for (int i = 0; i < num_list.length; i++){
            if (n == num_list.length){
                n -= num_list.length;
            }
            answer[i] = num_list[n];
            n += 1;
        }
        return answer;
    }
}