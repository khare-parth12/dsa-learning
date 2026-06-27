class Solution:
    def rev(self, nums, l, r):
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1

    def rotatearray(self, nums, k):
        self.rev(nums, 0, len(nums)-k)
        self.rev(nums, len(nums)-k, len(nums)-1)
        self.rev(nums, 0, len(nums)-1)