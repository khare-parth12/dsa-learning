# Leetcode 1314

class Solution(object):
    def matrixBlockSumBrute(self, mat, k):
        m = len(mat)
        n = len(mat[0])
        answer = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                Sum = 0

                for r in range(i-k, i+k+1):
                    for c in range(j-k, j+k+1):
                        if (r>=0 and r<m and c>=0 and c<n):
                            Sum += mat[r][c]

                answer[i][j] = Sum

        return answer

    # from (0,0) index
    def matrixBlockSum(self, mat, k):
        m = len(mat)
        n = len(mat[0])
        answer = [[0 for _ in range(n)] for _ in range(m)]
        prefix = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        Sum = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                prefix[i][j] = mat[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]

        for i in range(m):
            for j in range(n):
                r1 = max(0, i-k) + 1
                c1 = max(0, j-k) + 1
                r2 = min(m-1, i+k) + 1
                c2 = min(n-1, j+k) + 1

                answer[i][j] = prefix[r2][c2] - prefix[r1-1][c2] - prefix[r2][c1-1] + prefix[r1-1][c1-1]                        

        return answer

    #from (0,n) index

    # from (m,n) index
    
    # from (m,0) index    