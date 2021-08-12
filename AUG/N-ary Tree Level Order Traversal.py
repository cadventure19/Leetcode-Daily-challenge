class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        ans=[]
        queue=collections.deque()
        if root is not None:
            queue.append((root,0))
            
        
        while len(queue)>0:
            node,level=queue.popleft()
            
            if level+1>len(ans):
                ans.append([])
            ans[-1].append(node.val)
            
            for child in node.children:
                queue.append((child,level+1))
                
        return ans