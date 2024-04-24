class Solution {
    public int solution(String myString, String pat) {
        String newString = "";
        for (int i = 0; i < myString.length(); i++){
            if (myString.charAt(i) == 'A'){
                newString += "B";
            } else{
                newString += "A";
            }
        }
        if (myString.length() < pat.length()){
            return 0;
        }
        if (newString == pat){
            return 1;
        }
        int start = 0;
        int end = pat.length();
        
        while(end <= myString.length()){
            if (newString.substring(start,end).equals(pat)){
                return 1;
            }
            start += 1;
            end += 1;
        }
        
        return 0;
    }
}