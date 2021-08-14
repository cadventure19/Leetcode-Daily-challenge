class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if matrix is None:
            return 
        
        m=len(matrix)
        n=len(matrix[0])
        
        FirstRowHasZero=False
        FirstColHasZero=False
        
        
        def nullifyRow(matrix,i,m,n):
            for col in range(n):
                matrix[i][col]=0
                
        def nullifyCol(matrix,j,m,n):
            for row in range(m):
                matrix[row][j]=0
        
        for i in range(n):
            if matrix[0][i]==0:
                FirstRowHasZero=True
                break
                
        for i in range(m):
            if matrix[i][0]==0:
                FirstColHasZero=True
                break
                
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0
                    
        for i in range(1,n):
            if matrix[0][i]==0:
                nullifyCol(matrix,i,m,n)
        
        for i in range(1,m):
            if matrix[i][0]==0:
                nullifyRow(matrix,i,m,n)
                
                
        if FirstRowHasZero:
            nullifyRow(matrix,0,m,n)
            
        
        if FirstColHasZero:
            nullifyCol(matrix,0,m,n)
                
        return matrix