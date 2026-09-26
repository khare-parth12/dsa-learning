# Leetcode 11

class Solution(object):
    def maxArea(self, height):
        i, j = 0, len(height) - 1
        maxArea = 0

        while i < j:
            minHeight = min(height[i], height[j])
            currArea = minHeight * (j-i)
            maxArea = max(maxArea, currArea)
            
            if height[i] < height[j]: i += 1
            else: j -= 1

        return maxArea