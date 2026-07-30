package Hashing;

public class FreqMap {
    public static java.util.Map<Character, Integer> frequencyOfChar(String s){
        if (s == null || s.isEmpty()) return new java.util.HashMap<>();

        java.util.Map<Character, Integer> freq = new java.util.HashMap<>();
        for (char c: s.toCharArray()){
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }

        return freq;
    }

    public static void main(String[] args) {
        
    }
}
