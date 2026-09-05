public class CheckPalindrome {
    public static boolean isPalindrome(String s){
        if (s == null) return false;
        if (s.length() == 0 || s.length() == 1) return true;
        int left = 0;
        int right = s.length() - 1;

        while (left < right) {
            if (s.charAt(left) != s.charAt(right))
                return false;
            left++;
            right--;
        }
        return true;
    }

    public static boolean isPalindromeAlphanumeric(String s){
        if (s == null) return false;
        if (s.length() == 0 || s.length() == 1) return true;
        int left = 0;
        int right = s.length()-1;

        while (left<right){
            while (left<right && !Character.isLetterOrDigit(s.charAt(left))){
                left++;
            } while (left<right && !Character.isLetterOrDigit(s.charAt(right))){
                right--;
            }

            if (Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    public static boolean isPalindromerecursive(String s, int left, int right){
        if (left>=right) return true;
        if (s.charAt(left) != s.charAt(right)) return false;
        return isPalindromerecursive(s, left+1, right-1);
    }

    public static void main(String args[]){
        System.out.println(isPalindrome("racecar"));
    }    
}
