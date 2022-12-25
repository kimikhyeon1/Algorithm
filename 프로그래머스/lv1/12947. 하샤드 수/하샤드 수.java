class Solution {
    public boolean solution(int x) {
        String string = String.valueOf(x);

        int sum = 0;
        for (int i = 0; i < string.length(); i++) {
            char ch = string.charAt(i);
            int num = (int)ch-48;
            System.out.println(num);
            sum += num;
        }
        if (x%sum ==0){
            return true;
        } else return false;
    }
}