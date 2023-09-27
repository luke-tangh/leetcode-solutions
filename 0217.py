from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums) -> bool:
        dupe = defaultdict(int)
        for i in nums:
            if i in dupe:
                return True
            else:
                dupe[i] += 1
        return False
        # return len(nums) != len(set(nums))