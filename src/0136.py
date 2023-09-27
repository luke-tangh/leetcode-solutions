class Solution:
    def singleNumber(self, nums) -> int:
        ret = []
        for n in nums:
            try:
                ret.remove(n)
            except:
                ret.append(n)
        return ret[0]