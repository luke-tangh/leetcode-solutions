class Solution:
    def maxArea(self, height: list[int]) -> int:
        l, r = 0, len(height) - 1
        ans = 0
        while l < r:
            ans = max(ans, (r-l)*min(height[l], height[r]))
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return ans
