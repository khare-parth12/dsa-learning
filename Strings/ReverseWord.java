package Strings;

public class ReverseWord {
    public static String reverseWord(String s){
        if (s == null || s.isEmpty()) return s;
        if (s.length() == 1) return s;
                
        int j = 0;
        char[] str1 = new char[s.length()];
        for (int i=s.length()-1; i>=0; i--){
            str1[j] = s.charAt(i);
            j++;
        }
        return new String(str1);
    }

    public static void main(String[] args) {
        System.out.println(reverseWord("Parth"));
    }
    
}
