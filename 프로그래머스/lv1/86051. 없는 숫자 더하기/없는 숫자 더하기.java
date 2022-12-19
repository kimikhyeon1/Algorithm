import java.util.ArrayList;
import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        ArrayList<Integer> space = new ArrayList<>(Arrays.asList(1,2,3,4,5,6,7,8,9));
        for (int i =0; i<numbers.length; i++){
            space.remove(Integer.valueOf(numbers[i]));
        }
        for (int i = 0; i< space.size(); i++){
            answer += space.get(i);
        }
        return answer;
    }
}