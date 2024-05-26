class Solution {
    public int solution(int[] num_list) {
        int sum = 0;
        int multi = 1;
        for (int i = 0; i < num_list.length; i++){
            sum += num_list[i];
            multi *= num_list[i];
        }
        return sum * sum < multi ? 0 : 1;
    }
}