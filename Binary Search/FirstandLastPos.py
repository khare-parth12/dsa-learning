# Leetcode 34

class Solution(object):
    def searchRange(self, nums, target):
        def first(n1, t1):
            l, r = 0, len(n1) - 1
            x = -1
            while l <= r:
                mid = (l + r)//2
                if n1[mid] == t1:
                    x = mid
                    r = mid - 1
                elif n1[mid] > t1:
                    r = mid - 1
                else:
                    l = mid + 1

            return x

        def last(n2, t2):
            l, r = 0, len(n2) - 1
            y = -1
            while l <= r:
                mid = (l + r)//2
                if n2[mid] == t2:
                    y = mid
                    l = mid + 1
                elif n2[mid] > t2:
                    r = mid - 1
                else:
                    l = mid + 1

            return y
        
        i = first(nums, target)
        j = last(nums, target)

        return [i, j]