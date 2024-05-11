class Solution:


    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        

        res=[[float("inf")]*(n+1) for r in range(m+1)]
        res[m][n-1]=0
        res[m-1][n-1]=grid[m-1][n-1]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                res[i][j]=grid[i][j]+min(res[i][j+1],res[i+1][j])
        
        x=int(res[0][0])
        return x
                

                


        
        
        
