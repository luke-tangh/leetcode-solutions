class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        high = alt = 0
        for n in gain:
            alt += n
            high = max(high, alt)
        return high
