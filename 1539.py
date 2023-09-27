class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        last = 0
        for n in arr:
            if n - last > 1:
                k -= n - last - 1
                last = n
                if k <= 0:
                    last -= 1
                    break
            else:
                last = n
        return last + k
