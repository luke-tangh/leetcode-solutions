class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        n = "123456789"
        ret = []
        for i in range(len(str(low)), len(str(high)) + 1):
            for j in range(10 - i):
                seg = int(n[j:j + i])
                if low <= seg <= high:
                    ret.append(seg)
        return ret
