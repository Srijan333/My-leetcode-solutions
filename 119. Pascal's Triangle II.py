class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        r=rowIndex
        res=[[1],[1,1]]

        if(r<2):
            return res[r]
        else:
            res1=[[0]*i for i in range(1,r+2)]
            print(res1)
            res1[0][0]=1
            for i in range(1,r+1):
                l=len(res1[i])
                res1[i][0]=1
                res1[i][l-1]=1
            for i in range(2,r+1):
                for j in range(len(res1[i])):
                    if(res1[i][j]==0):
                        res1[i][j]=res1[i-1][j-1]+res1[i-1][j]
            print(res1)
            return res1[r]
        
