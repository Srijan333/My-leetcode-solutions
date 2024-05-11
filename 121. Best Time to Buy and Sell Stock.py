class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=len(prices)
        mi=prices[0]
        ma=0
        ans=0
        for i in range(0,l-1):
            mi=prices[i]
            ma=max(prices[i+1:l])
            m=ma-mi
            if(m>ans):
                ans=m
            
        return ans




/* 
for i in range(0,l-1):
            for j in range(i,l):
                mi=prices[i]
                ma=prices[j]
                m=ma-mi
                if(m>ans):
                    ans=m
        return ans
*/
