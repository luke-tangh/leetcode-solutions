class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        S, D = map(set, zip(*paths))
        return (D - S).pop()
