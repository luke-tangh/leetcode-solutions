class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        fst = snd = 101
        for p in prices:
            if p < snd:
                if p < fst:
                    snd = fst
                    fst = p
                else:
                    snd = p
        ret = money - fst - snd
        return ret if ret >= 0 else money
