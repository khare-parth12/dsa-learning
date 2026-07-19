public class Power {
    public static double powerIterative(double x, int n) {
        long N = n;
        if (N < 0){
            x = 1.0/x;
            N = -N;
        }

        double result = 1;
        while (N > 0) {
            if (N%2==1) result = result * x;
            x *= x;
            N /= 2;
        }

        return result;
    }

    public static void main(String args[]){
        System.out.println(powerIterative(5, 4));
        System.out.println(powerIterative(5, -4));
    }
}
