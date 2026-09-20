# Leetcode 69

class Solution(object):
    def mySqrt(self, x):
        if x==0: return 0

        low = 1
        high = x

        while low <= high:
            mid = (low + high)/2
            if mid*mid == x:
                return mid

            if mid*mid < x:
                low = mid+1
            
            if mid*mid > x:
                high = mid-1

        return high