import java.util.*;
class Solution {
    public int[] solution(int[] num_list) {
        int length = num_list.length - 5;
        int[] answer = new int[length];
        Arrays.sort(num_list);
        int temp = 5;
        for (int i = 0; i < answer.length; i++){
            answer[i] = num_list[temp];
            temp += 1;
        }
        return answer;
    }
}