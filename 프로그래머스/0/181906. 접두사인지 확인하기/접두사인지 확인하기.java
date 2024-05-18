class Solution {
    public int solution(String my_string, String is_prefix) {
        int minIndex = my_string.length() < is_prefix.length() ? my_string.length() : is_prefix.length();
        
        if (my_string.length() < is_prefix.length()){
            return 0;
        }
        for (int i = 0; i < minIndex; i++){
            if (my_string.charAt(i) != is_prefix.charAt(i)){
                return 0;
            }
            
        }
        return 1;
    }
}