// Leetcode 796

import java.util.Arrays;

public class RotateString {
    public boolean rotateString(String s, String goal) {
        if (s.length() != goal.length()) return false;

        char[] c1 = s.toCharArray();
        char[] c2 = goal.toCharArray();

        int len = c1.length;
        for (int i=0; i<len; i++){
            char[] c3 = Arrays.copyOfRange(c1, 1, len+1);
            c3[len-1] = c1[0];
            if (String.valueOf(c3).equals(String.valueOf(c2))) return true;
            c1 = c3;
        }
        return false;
    }

    public static void main(String[] args) {
        
    }
}
