class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        t = len(arr) // 4
        for i in range(len(arr) - t):
            if arr[i] == arr[i + t]:
                return arr[i]
        return 0
