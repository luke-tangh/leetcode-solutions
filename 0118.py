class Solution:
    def generate(self, numRows: int):
        tria = [[] for i in range(numRows)]
        tria[0] = [1]
        for i in range(numRows-1):
            tria[i+1].append(1)
            for j in range(len(tria[i])-1):
                tria[i+1].append(tria[i][j]+tria[i][j+1])
            tria[i+1].append(1)
        return tria