class Solution {
    public int[] solution(int[] num_list, int n) {
        int[] answer = new int[num_list.length - n + 1];
        int index = n - 1;
        for(int i = 0; i < num_list.length - n + 1; i++){
            answer[i] =  num_list[index];
            index++;
            System.out.println(n);
        }
        return answer;
    }
}