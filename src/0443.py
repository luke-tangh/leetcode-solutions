class Solution:
    def compress(self, chars: list[str]) -> int:
        last = ""
        head = 0
        count = 1
        for i in range(len(chars)):
            if chars[i] == last:
                count += 1
                continue
            if count > 1:
                for c in list(str(count)):
                    chars[head] = c
                    head += 1
                count = 1
            last = chars[i]
            chars[head] = chars[i]
            head += 1
        if count > 1:
            for c in list(str(count)):
                chars[head] = c
                head += 1
        chars = chars[0:head]
        return head
