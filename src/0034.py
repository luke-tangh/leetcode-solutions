class Solution:
    def searchRange(self, nums, target: int):
        if len(nums) < 1:
            return [-1, -1]
        found = searchfailed = False
        first = 0
        last = len(nums) - 1
        while not found and not searchfailed:
            middle = (first + last) // 2
            if nums[middle] == target:
                found = True
            else:
                if first >= last:
                    searchfailed = True
                else:
                    if nums[middle] > target:
                        last = middle - 1
                    else:
                        first = middle + 1
        if found:
            left = right = middle
            while left >= 0 and nums[left] == target:
                left -= 1
            while right < len(nums) and nums[right] == target:
                right += 1   
            return [left+1, right-1]
        else:
            return [-1, -1]
