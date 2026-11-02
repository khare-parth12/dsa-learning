# Leetcode 739

class Solution(object):
    def dailyTemperatures(self, temps):
        n = len(temps)
        ans = [0] * n
        idx = []
        
        for i, temp in enumerate(temps):
            while idx and temps[idx[-1]] < temp:
                index = idx.pop()
                ans[index] = i - index
            idx.append(i)

        return ans