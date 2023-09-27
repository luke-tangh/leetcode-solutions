class Solution:
    def permute(self, nums):
        ret = []
        ret = Solution.swift(self, nums, [], ret)
        return ret
    
    def swift(self, spare, occup, res):
        if not spare:
            res.append(occup)
        else:
            for i in range(len(spare)):
                self.swift(spare[:i]+spare[i+1:], occup+[spare[i]], res)
        return res