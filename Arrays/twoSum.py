class Solution:
    def twosum(self, nums, target):
        seen = {}
        for i, n in enumerate(nums):
            compliment = target - n
            if compliment in seen:
                return [seen[compliment], i]
            seen[n] = i