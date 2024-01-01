class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g.sort()
        s.sort()
        pg = ps = 0
        while ps < len(s) and pg < len(g):
            if g[pg] <= s[ps]:
                pg += 1
            ps += 1
        return pg
