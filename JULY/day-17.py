class Solution(object):
    def threeEqualParts(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ans=[-1,-1]
        n=0
        for i in arr:
            if i==1:
                n+=1
        
        if n==0:
            return [0,2]
        
        if n%3!=0:
            return ans
        
        each_part_one=n/3
        index_first_one_first=-1
        index_first_one_second=-1
        index_first_one_third=-1
        
        no_ones=0
        for i in range(len(arr)):
            if arr[i]==1:
                no_ones+=1
                if no_ones==each_part_one+1:
                    index_first_one_second=i
                    
                if no_ones==2*(each_part_one)+1:
                    index_first_one_third=i
                    
                if no_ones==1:
                    index_first_one_first=i
        print(index_first_one_first,index_first_one_second,index_first_one_third)
        
        while index_first_one_third<len(arr):
            if arr[index_first_one_third]==arr[index_first_one_second] and arr[index_first_one_third]==arr[index_first_one_first]:
                index_first_one_first+=1
                index_first_one_second+=1
                index_first_one_third+=1
            
            else:
                return ans
        return [index_first_one_first-1, index_first_one_second]
                
        
                
