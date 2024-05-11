class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(ord('Z'))

        s=list(s)
        anss=[]
        for i in s:
            if( (97<=ord(i)<=122) or (65<=ord(i)<=90) or 48<=ord(i)<=57 ):
                anss.append(i.lower())
        
      

        res=(anss==anss[::-1])
        return res

