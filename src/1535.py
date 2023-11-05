class Solution:
    def getWinner(self, arr: list[int], k: int) -> int:
        wins = cur = 0
        idx = 1
        if k > len(arr):
            return max(arr)
        while wins < k:
            if cur == idx:
                idx += 1
                continue
            if idx >= len(arr):
                idx = 0
                continue
            if arr[cur] > arr[idx]:
                idx += 1
                wins += 1
            else:
                wins = 1
                cur = idx
                idx += 1
        return arr[cur]
