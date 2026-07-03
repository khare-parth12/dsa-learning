public class CountVowels {
    public static int CntVowels(String s){
        if (s == null || s.isEmpty())  return 0;

        java.util.Set<Character> vowels = new java.util.HashSet<>(
            java.util.Arrays.asList('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        );

        int count = 0;
        for (char c: s.toCharArray()){
            if (vowels.contains(c)) count++;
        }

        return count;
    }

    public static int CntVowelsLower(String s){
        if (s == null || s.isEmpty()) return 0;

        int count = 0;
        for (char c: s.toLowerCase().toCharArray()){
            if ("aeiou".indexOf(c) != -1) count++;
        }
        return count;
    }

    public static void main(String args[]){
        System.out.println(CntVowels("Hello World"));
        System.out.println(CntVowelsLower("Hello World"));

    }
}
