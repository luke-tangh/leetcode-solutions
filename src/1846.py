class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: list[int]) -> int:
        arr.sort()
        prev = 0
        for i in range(len(arr)):
            if arr[i] > prev:
                arr[i] = prev + 1
            prev = arr[i]
        return arr[-1]
