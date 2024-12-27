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

        q=deque([root])
        res=[]
        while q:
            curr_length=len(q)
            level_sum=0
            for _ in range(curr_length):
                
                curr=q.popleft()
                level_sum+=curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                
            
            avg=level_sum/curr_length
            res.append(avg)
        
        return res
