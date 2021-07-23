class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        N=len(dominoes)
        left=[0]*N
        right=[0]*N
        nearest_left_index=-1
        for i in range(N-1,-1,-1):
            if dominoes[i]=='L':
                nearest_left_index=i
                
            elif dominoes[i]=='R':
                nearest_left_index=-1
                
            left[i]=nearest_left_index
            
        nearest_right_index=-1
        for i in range(N):
            if dominoes[i]=='R':
                nearest_right_index=i
                
            elif dominoes[i]=='L':
                nearest_right_index=-1
            right[i]=nearest_right_index
            
        ans=[0]*N
        max_value=10**10
        for i in range(N):
            if dominoes[i]=='.':
                nearest_left=left[i]
                nearest_right=right[i]
            
                if left[i]==-1:
                    leftDiff=max_value
                else:
                    leftDiff=abs(nearest_left-i)
                
                if right[i]==-1:
                    rightDiff=max_value
                else:
                    rightDiff=abs(nearest_right-i)
                    
                    

            
                if leftDiff==rightDiff:
                    ans[i]='.'
                elif leftDiff<rightDiff:
                    ans[i]='L'
                elif leftDiff>rightDiff:
                    ans[i]='R'
                
            else:
                ans[i]=dominoes[i]

        return ''.join(str(i) for i in ans)
                
                

            
            
            