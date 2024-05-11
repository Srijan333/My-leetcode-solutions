class Solution:
    def romanToInt(self, s: str) -> int:

        d={'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000}
        s=list(s)
        l=len(s)
        sum=0

        for i in range(0,l-1):
            if d[s[i+1]]<=d[s[i]]:
                sum+=int(d[s[i]])
            elif d[s[i+1]]>d[s[i]]:
                sum=sum-int(d[s[i]])
            print(sum)
        sum+=d[s[l-1]]
        
        return sum

