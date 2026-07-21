import java.util.Arrays;

public class MaxMinElement {
    public static int sumOfDigits(int num) {
        num = Math.abs(num);

        if (num < 10)
            return num;
        return num % 10 + sumOfDigits(num / 10);
    }

    public static int minEleIterative(int[] nums){
        int n = nums.length;
        int minNum = Integer.MAX_VALUE;
        for (int i=0; i<n; i++){
            nums[i] = sumOfDigits(nums[i]);
            minNum = Math.min(minNum, nums[i]);
        }

        return minNum;
    }

    public static void main(String args[]){
        int[] nums = {123, 432, 765, 345, 987};
        System.out.println(minEleIterative(nums));
    } 
}
