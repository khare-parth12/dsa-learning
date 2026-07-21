public class Power {
    public static double myPow(double x, int n){
        long N = n;
        if (N<0){
            x = 1.0/x;
            N = -N;
        }
        return fastPow(x, N);
    }

    public static double fastPow(double x, long N){
        if (N==0) return 1.0;

        if (N%2==0){
            double half = fastPow(x, N/2);
            return half * half;
        }else {
            return x * fastPow(x, N-1);
        }
    }

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
