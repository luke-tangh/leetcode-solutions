class Solution:
    def productExceptSelf(self, nums):
        ret = []
        arrsum = 1        
        count = nums.count(0)
        if count == 1:
            for n in nums:
                if n:
                    arrsum *= n
            for n in nums:
                if n:
                    ret.append(0)
                else:
                    ret.append(arrsum)
            return ret
        elif count > 1:
            return [0 for i in range(len(nums))]
        else:
            for n in nums:
                arrsum *= n
            for n in nums:
                ret.append(int(arrsum/n))
            return ret