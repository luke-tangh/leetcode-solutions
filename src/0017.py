class Solution:
    def letterCombinations(self, digits):
        trans = {
                '2' : ["a","b","c"],
                '3' : ["d","e","f"],
                '4' : ["g","h","i"],
                '5' : ["j","k","l"],
                '6' : ["m","n","o"],
                '7' : ["p","q","r","s"],
                '8' : ["t","u","v"],
                '9' : ["w","x","y","z"]
                }
        if digits == "":
            return []
        ret = trans[digits[0]]
        for n in digits[1:]:
            ret = Solution.permutation(self, trans[n], ret)
        return ret

    def permutation(self, n, s):
        r = []
        for i in n:
            for j in s:
                r.append(j+i)
        return r
