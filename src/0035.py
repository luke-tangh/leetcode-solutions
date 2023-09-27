class Solution:
    def searchInsert(self, nums, target: int) -> int:
        found = False
        searchfailed = False
        first = 0
        last = len(nums) - 1
        while not found and not searchfailed:
            middle = (first+last) // 2
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
            return middle
        else:
            return first + 1 if nums[first] <= target else first 
