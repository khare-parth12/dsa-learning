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
        if (s == null || s.isEmpty()) return s;

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
        if (s == null || s.isEmpty()) return s;

        s = s.trim();
        StringBuilder result = new StringBuilder();
        int right = s.length() - 1;

        while (right>=0){
            while (right>=0 && s.charAt(right) == ' ') right--;
            if (right<0) break;
            
            int end = right;
            while (right>=0 && s.charAt(right) != ' ') right--;

            result.append(s, right+1, end-1);
            if (right>=0) result.append(' ');
        }

        return result.toString();
    }

    public static void reverseChar(char[] c, int left, int right){
        while (left<right){
            char temp = c[left];
            c[left] = c[right];
            c[right] = temp;
            left++;
            right--;
        }
    }

    public static String reverseEachWord(String s){
        if (s == null || s.isEmpty()) return s;

        char[] c = s.toCharArray();
        int start = 0;

        for (int i= 0; i <= c.length; i++){
            if (i == c.length || c[i] == ' '){
                reverseChar(c, start, i-1);
                start = start + i;
            }
        }
        return new String(c);
    }

    public static String reverseWordsInPlace(String s){
        if (s == null || s.isEmpty()) return s;

        char[] c = s.trim().toCharArray();
        int start = 0;

        reverseChar(c, 0, c.length-1);

        for (int i = 0; i <= c.length; i++) {
            if (i == c.length || c[i] == ' ') {
                reverseChar(c, start, i - 1);
                start = start + i;
            }
        }
        return new String(c);
    }

    public static void main(String[] args) {
        System.out.println(reverseString("Parth"));
    }
    
}
