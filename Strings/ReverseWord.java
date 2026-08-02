package Strings;

public class ReverseWord {
    public static String reverseString(String s){
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

    public String reverseWords(String s) {
        if (s == null || s.isEmpty())
            return s;

        String[] words = s.trim().split("\\s+");
        int left = 0, right = words.length - 1;

        while (left < right) {
            String temp = words[left];
            words[left] = words[right];
            words[right] = temp;
            left++;
            right--;
        }
        return String.join(" ", words);
    }

    public String reverseWordManual(String s){
        
    }

    public static void main(String[] args) {
        System.out.println(reverseString("Parth"));
    }
    
}
