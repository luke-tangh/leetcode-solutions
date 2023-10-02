class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack = []
        mid = -10**10

        for n in reversed(nums):
            if n < mid:
                return True
            while stack and stack[-1] < n:
                mid = stack.pop()
            stack.append(n)
        return False
        