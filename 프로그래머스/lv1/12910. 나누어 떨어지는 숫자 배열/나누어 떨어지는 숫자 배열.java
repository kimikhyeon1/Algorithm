import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] % divisor == 0) {
                answer.add(arr[i]);
            }
        }
        if (answer.size()==0) {
            answer.add(-1);
        } else {
            Collections.sort(answer);
        }
        int[] a1 = {};
        a1 = new int[answer.size()];
        for( int i =0; i<answer.size();i++){
            a1[i] = answer.get(i);
        }
        return a1;
}
}