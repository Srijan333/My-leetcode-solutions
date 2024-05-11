class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows
        res=[[0]*i for i in range(1,n+1) ]
        res[0][0]=1
        for i in range(1,n):
            l=len(res[i])
            res[i][0]=1
            res[i][l-1]=1
        for i in range(2,n):
            for j in range(len(res[i])):
                if(res[i][j]==0):
                    res[i][j]=res[i-1][j-1]+res[i-1][j]
        return res
