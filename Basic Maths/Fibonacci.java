public class Fibonacci{
    public static long fibRecursive(int n){
        if (n<0) throw new IllegalArgumentException("Give Positive value as input.");
        if (n==0) return 0;
        if (n==1) return 1;
        return fibRecursive(n-1) + fibRecursive(n-2);
    }

    public static long fibIterative(int n){
        if (n < 0) throw new IllegalArgumentException("Give Positive value as input.");
        if (n == 0) return 0;
        if (n == 1) return 1;

        long prev2 = 0, prev1 = 1;
        for (int i =2; i<=n; i++){
            long curr = prev2 + prev1;
            prev2 = prev1;
            prev1 = curr;
        }

        return prev1;
    }

    public static void main(String args[]){

    }
}