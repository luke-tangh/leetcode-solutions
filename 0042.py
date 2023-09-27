class Solution:
    def trap(self, height: list[int]) -> int:
        if len(height) <= 2:
            return 0
        maxl, maxr = height[0], height[-1]
        l, r = 1, len(height) - 2
        ans = 0
        while r >= l:
            if maxr > maxl:
                if height[l] > maxl:
                    maxl = height[l]
                else:
                    ans += maxl - height[l]
                l += 1
            else:
                if height[r] > maxr:
                    maxr = height[r]
                else:
                    ans += maxr - height[r]
                r -= 1
        return ans