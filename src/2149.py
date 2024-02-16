class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans = [0 for _ in range(len(nums))]
        pos, neg = 0, 1
        for n in nums:
            if n > 0:
                ans[pos] = n
                pos += 2
            else:
                ans[neg] = n
                neg += 2
        return ans
