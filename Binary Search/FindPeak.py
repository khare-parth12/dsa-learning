# Leetcode 162

class Solution(object):
    def findPeakElement(self, nums):
        if len(nums) == 1: return 0

        if len(nums) > 1 and (nums[0] > nums[1]): return 0
        elif len(nums) > 1 and (nums[len(nums)-1] > nums[len(nums)-2]): return len(nums)-1
        else:
            peak_el = 0
            left, right = 1, len(nums)-2
            while left <= right:
                mid = (left + right)//2
                if (nums[mid]>nums[mid+1]) and (nums[mid]>nums[mid-1]): return mid
                elif nums[mid] > nums[mid+1]:
                    right = mid
                else:
                    left = mid + 1 