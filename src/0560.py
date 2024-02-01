from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        hashmap = defaultdict(int)
        hashmap[0] = 1
        count = 0
        prefix_sum = 0
        for n in nums:
            prefix_sum += n
            target = prefix_sum - k
            count += hashmap[target]
            hashmap[prefix_sum] += 1
        return count
