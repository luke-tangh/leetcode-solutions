# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return

class Solution:
    def firstBadVersion(self, n: int) -> int:
        self.p = n//2 + 1
        self.upper = n
        self.lower = 1
        return self.search()

    
    def search(self):
        if isBadVersion(self.p):
            if not isBadVersion(self.p-1):
                return self.p
            self.upper = self.p
            self.p = (self.lower + self.p) // 2
            self.search()
        else:
            self.lower = self.p
            self.p = ((self.upper + self.p) // 2) + 1
            self.search()
        return self.p