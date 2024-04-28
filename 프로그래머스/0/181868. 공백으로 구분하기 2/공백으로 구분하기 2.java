import java.util.Arrays;
class Solution {
    public String[] solution(String my_string) {
        my_string = my_string.trim();
        String space = "";
        int arraySize = 1;
        for (int i = 0; i < my_string.length(); i++){
            char ch = my_string.charAt(i);
            
            if (ch == ' ' && space.length() > 0){
                space = "";
                arraySize += 1;
                continue;
            }
            
            if (ch == ' '){
                continue;
            }
            
            space += ch;
        }
        
        String[] answer = new String[arraySize];
        String temp = "";
        int index = 0;
        
        for (int i = 0; i < my_string.length(); i++){
            char ch = my_string.charAt(i);
            
            if (ch == ' ' && temp.length() > 0){
                answer[index] = temp;
                temp = "";
                index += 1;
                continue;
            }
            
            if (ch == ' '){
                continue;
            }
            
            temp += ch;
        }
        
        if (temp.length() > 0){
            answer[index] = temp;
        }

        return answer;
    }
}