class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        if matrix[0][0] > target:
            return False
        elif matrix[len(matrix)-1][len(matrix[0])-1] < target:
            return False
        tarlist = []
        for i in range(len(matrix)):
            if target == matrix[i][0]:
                return True
            elif target < matrix[i][0]:
                if i == 0:
                    return False
                else:
                    tarlist = matrix[i-1]
                    break
        if not tarlist:
            tarlist = matrix[len(matrix)-1]
        return self.search(tarlist, target)
            
    def search(self, nums, target):
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
        return found