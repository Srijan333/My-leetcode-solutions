class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        n3=nums1+nums2
        n3=sorted(n3)
        n=[]
        n=nums1+nums2
        n=n.sort()

        l=len(n3)
        m=0.0
        print(n3)
        if l%2==1:
            h=(l+1)/2
            m=n3[h-1]
        else:
            m=(n3[(l)/2]+n3[(l/2)-1])
            m=m/2.0
            
            

        return m
