public class SumOfDigits{
    public static int sumIterative(int num){
        num = Math.abs(num);

        int sum = 0;
        while (num>0){
            sum += num%10;
            num = num/10;
        }

        return sum;
    }

    public static int sumRecursive(int num){
        num = Math.abs(num);

        if (num<10) return num;
        return num%10 + sumRecursive(num/10);
    }

    public static void main(String args[]){
        System.out.println(sumIterative(-123));
        System.out.println(sumRecursive(456));
    }
}