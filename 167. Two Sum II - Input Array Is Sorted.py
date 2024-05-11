class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l=len(numbers)
        t=target

        s=0
        e=l-1
        ans=[]

        while(s<e):
            if (numbers[s]+numbers[e])<t:
                s+=1
            elif (numbers[s]+numbers[e])>t:
                e-=1

            elif (numbers[s]+numbers[e])==t:
                print(s+1,e+1)
                ans.append(s+1)
                ans.append(e+1)
                s+=1
                e-=1

        
        return ans
