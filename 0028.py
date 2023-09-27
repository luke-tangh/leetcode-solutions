class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        head = tail = 0
        while tail < len(haystack) - len(needle) + 1:
            if head-tail == len(needle):
                return tail
            if haystack[head] == needle[head-tail]:
                head += 1
            else:
                tail += 1
                head = tail
        return tail if head-tail == len(needle) else -1
    