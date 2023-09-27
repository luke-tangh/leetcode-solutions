class Solution:
    def getRow(self, rowIndex: int):
        tria = [[] for i in range(rowIndex+1)]
        tria[0] = [1]
        for i in range(rowIndex):
            tria[i+1].append(1)
            for j in range(len(tria[i])-1):
                tria[i+1].append(tria[i][j]+tria[i][j+1])
            tria[i+1].append(1)
        return tria[rowIndex]