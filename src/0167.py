class Solution:
    def twoSum(self, numbers, target: int):
        imax = len(numbers) - 1
        imin = 0
        res = numbers[imin] + numbers[imax]
        while res != target:
            if res > target:
                imax -= 1
            else:
                imin += 1
            res = numbers[imin] + numbers[imax]
        return [imin + 1, imax + 1]