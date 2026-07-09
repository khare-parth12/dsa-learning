public class ReverseNumber {
    public static int reverse(int n){
        boolean neg = n<0;
        if (neg) n = Math.abs(n);

        int reverse = 0;
        while (n>0){
            int digit = n%10;

            if (reverse > (Integer.MAX_VALUE - digit)/10) return 0;

            reverse = reverse*10 + digit;
            n = n/10;
        }

        return neg? -reverse : reverse;
    }

    public static void main(String[] args) {
        System.out.println(reverse(543));
    }
}