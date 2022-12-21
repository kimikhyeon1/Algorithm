class Solution {
    public boolean solution(int x) {
        String string = String.valueOf(x);

        int sum = 0;
        for (int i = 0; i < string.length(); i++) {
            char ch = string.charAt(i);
            int num = Character.getNumericValue(ch);
            sum += num;
        }
        if (x%sum ==0){
            return true;
        } else return false;
    }
}