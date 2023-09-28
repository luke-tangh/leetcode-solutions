class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        index = length = 0
        while length < k:
            if s[index].isdigit():
                length *= int(s[index])
            else:
                length += 1
            index += 1
        for index in range(index - 1, -1, -1):
            if s[index].isdigit():
                length //= int(s[index])
                k %= length
            else:
                if k == 0 or k == length:
                    return s[index]
                length -= 1
