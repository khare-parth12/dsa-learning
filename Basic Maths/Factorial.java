public class Factorial {
    public static long factIterative(int n){
        if (n<0) throw new IllegalArgumentException("Negative input given. Factorial not possible");
        int result = 1;

        for (int i = 2; i<=n; i++){
            result = result * i;
        }

        return result;
    }

    public static long factRecursive(int n) {
        if (n < 0) throw new IllegalArgumentException("Negative input given. Factorial not possible");

        if (n==0 || n==1) return 1;
        return n * factRecursive(n-1);
    }

    public static void main(String args[]){
        System.out.println(factIterative(5));
        System.out.println(factRecursive(6));
    }
}
