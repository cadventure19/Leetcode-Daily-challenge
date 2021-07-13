class Solution(object):
    def findPeakElement(self, nums):
        a=len(nums)
        if a==1:
            return 0
        if a==2:
            if nums[1]>nums[0]:
                return 1
        if nums[a-1]>nums[a-2]:
            return a-1
            
            
        for i in range(1,a-1):
            if nums[i-1]<nums[i]:
                b=nums[i]
                if b>nums[i+1]:
                    return i
        
        return 0