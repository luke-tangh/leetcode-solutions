class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        def is_arith(ns: list[int]) -> bool:
            ns.sort()
            diff = ns[1] - ns[0]
            for i in range(1, len(ns) - 1):
                if ns[i + 1] - ns[i] != diff:
                    return False
            return True
        ret = []
        for (i, j) in zip(l, r):
            ret.append(is_arith(nums[i:j + 1]))
        return ret
