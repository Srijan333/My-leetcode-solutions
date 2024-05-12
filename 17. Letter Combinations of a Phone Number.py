class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters={
            '2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv',
            '9':'wxyz'
        }
        res=[]
        ans=[]
        n=len(digits)
        def backt(i=0):
            if i==n:
                if(len(ans)==0):
                    return
                else:
                    res.append("".join(ans))
                    return
            
            for letter in letters[digits[i]]:
                ans.append(letter)
                print(ans)
                backt(i+1)
                ans.pop()
        backt()

        return res





        
