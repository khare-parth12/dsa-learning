# Leetcode 485

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt = 0
        max_cnt = 0
        left = 0
        
        for right in range(len(nums)):
            if nums[right]==1:
                cnt += 1

            if (nums[right] == 0) or (right == len(nums)-1):
                max_cnt = max(max_cnt, cnt)
                cnt = 0 
                left = right + 1

        return max_cnt