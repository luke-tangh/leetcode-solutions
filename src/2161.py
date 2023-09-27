class Solution:
    def pivotArray(self, nums: list[int], pivot: int) -> list[int]:
        left = []; right = []
        pivs = 0
        for n in nums:
            if n == pivot:
                pivs += 1
            elif n < pivot:
                left.append(n)
            else:
                right.append(n)
        return left + [pivot]*pivs + right
