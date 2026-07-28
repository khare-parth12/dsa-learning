package Strings;

public class ReverseWord {
    public static String reverseWord(String s){
        if (s == null) return "";
        if (s.length() == 0 || s.length() == 1) return s;
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            
            left++;
            right--;
        }
        return true;
    }
    public static void main(String[] args) {
        
    }
    
}
