class Solution:
    def jump(self, nums: list[int]) -> int:
        jumps = last_jump = max_idx = i = 0
        while last_jump < len(nums) - 1:
            max_idx = max(max_idx, i + nums[i])
            if i == last_jump:
                last_jump = max_idx
                jumps += 1
            i += 1
            print(i, jumps, last_jump, max_idx)
            input()
        return jumps

sample = [3,4,3,2,1,2]
Solution().jump(sample)
