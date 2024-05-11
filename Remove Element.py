class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        l=len(nums)
        c=0
        n=nums
        count = 0
        for i in range(l):
            if n[i] != val:
                nums[c] = n[i]
                c+= 1
        return c
         
        
