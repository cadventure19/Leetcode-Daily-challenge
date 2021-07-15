class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums=[float('-inf')]+nums+[float('-inf')]
        n=len(nums)
        left=1
        right=n-2
        
        while left<right:
            mid=(left+right)//2
            if nums[mid-1]<nums[mid] and nums[mid]>nums[mid+1]:
                return mid-1
            
            
            if nums[mid-1]>nums[mid]:
                right=mid
            
            else:
                left=mid+1
        return left-1