from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: list[list[int]], target: int) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])

        for row in matrix:
            for col in range(cols - 1):
                row[col + 1] += row[col]
        
        count = 0
        for i in range(cols):
            for j in range(i, cols):
                hashmap = defaultdict(int)
                hashmap[0] = 1
                cur_sum = 0
                for k in range(rows):
                    cur_sum += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    count += hashmap[cur_sum - target]
                    hashmap[cur_sum] += 1
        return count
