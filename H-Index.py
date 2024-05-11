class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()  //sort the list
        l=len(citations)
        c=0

        if(l==1 and citations[l-1]>=1):
            return 1

        for i in citations:
            h=l-c                  //calculating number of remaining elements(papers) from position i
            if(i>=h):              //check if no of citations for each paper is >= no of papers
                break
            c+=1
        
        ans=l-c
        return ans


