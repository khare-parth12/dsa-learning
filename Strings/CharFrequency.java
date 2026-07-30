package Strings;

public class CharFrequency {
    public static java.util.Map<Character, Integer> frequencyOfChar(String s){
        if (s == null || s.isEmpty()) return new java.util.HashMap<>();

        java.util.Map<Character, Integer> freq = new java.util.HashMap<>();
        for (char c: s.toCharArray()){
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        return freq;
    }

    public static int[] frequencyArray(String s){
        if (s == null || s.isEmpty()) return new int[26];

        int[] freq = new int[26];
        for (char c: s.toCharArray()){
            freq[c - 'a']++;
        }
        return freq;
    }

    public static int frequencyOf(String s, char target){
        if (s == null || s.isEmpty()) return 0;

        int count = 0;
        for (char c: s.toCharArray()){
            if (c == target){
                count++;
            }
        }
        return count;
    }

    public static void main(String[] args) {
        System.out.println(frequencyOf("i am a poet", 'a'));
        
        int[] arr = frequencyArray("banana");
        System.out.println("a=" + arr[0] + " b=" + arr[1] + " n=" + arr[13]);
    }
}
