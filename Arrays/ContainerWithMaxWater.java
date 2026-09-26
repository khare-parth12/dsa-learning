// Leetcode 11

class ContainerWithMaxArea {
    public int maxArea(int[] height) {
        int i = 0;
        int j = height.length - 1;
        int maxArea = 0;

        while (i < j){
            int minHeight = Math.min(height[i], height[j]);
            int currArea = minHeight * (j - i);
            maxArea = Math.max(currArea, maxArea);

            if (height[i] < height[j]) i++;
            else j--;
        }

        return maxArea;
    }
}