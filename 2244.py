from collections import Counter

class Solution:
    def minimumRounds(self, tasks: list[int]) -> int:
        taskmap = Counter(tasks)
        rounds = 0
        for v in taskmap.values():
            if v < 2:
                return -1
            if v == 2:
                rounds += 1
            else:
                if v % 3 == 0:
                    rounds += v // 3
                else:
                    rounds += v // 3 + 1
        return rounds
