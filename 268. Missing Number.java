import java.util.Arrays;
class Solution {
    public int missingNumber(int[] nums) {
        
        
        int l=nums.length;
        int as=0;
        int cs=0;

        

        for(int i=0;i<l;i++){
            cs=cs+i+1;
            as=as+nums[i];
        }

        return cs-as;

        
    }
}
