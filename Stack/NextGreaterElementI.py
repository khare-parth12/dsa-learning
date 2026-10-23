# Leetcode 496

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        nextGrt = {}
        stk = []
        for i in range(len(nums2)-1, -1, -1):
            while stk and stk[-1] <= nums2[i]:
                stk.pop()

            nextGrt[nums2[i]] = stk[-1] if stk else -1
            stk.append(nums2[i])

        ans = []
        for n in nums1:
            ans.append(nextGrt[n])

        return ans