class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bi = {
            "1" : True,
            "0" : False
            }
        carry, bit = 0, 0
        res = ""
        a = a.rjust(max(len(a),len(b)),"0")
        b = b.rjust(max(len(a),len(b)),"0")
        for i in range(1,len(a)+1):
            if bi[a[-i]] and bi[b[-i]]:
                bit = 2
            else:
                if bi[a[-i]] or bi[b[-i]]:
                    bit = 1
                else:
                    bit = 0
            if carry+bit == 3:
                carry = 1
                bit = 1
            elif carry+bit == 2:
                carry = 1
                bit = 0
            elif carry+bit == 1:
                carry = 0
                bit = 1
            else:
                carry = 0
                bit = 0
            res = str(bit) + res
        return "1" + res if carry == 1 else res