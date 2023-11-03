class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        ops = []
        cur = 1
        for i in range(len(target)):
            while (cur < target[i]):
                ops.append("Push")
                ops.append("Pop")
                cur += 1
            ops.append("Push")
            cur += 1
        return ops
