# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        #bfs

        q=deque()
        q.append(root)
        res=[]
        while q:
            currlength=len(q)
            avg=0
            for i in range(currlength):
                
                curr=q.popleft()
                avg+=curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
            
            avg=avg/currlength
            res.append(avg)
        
        return res
