# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        res=[]

        curr_level=[root]

        while curr_level:
            new_level=[]
            level_sum=0
            for n in curr_level:

                level_sum+=n.val
                if n.left:
                    new_level.append(n.left)
                if n.right:
                    new_level.append(n.right)
            
            level_avg=level_sum/len(curr_level)
            res.append(level_avg)
            curr_level=new_level
        return res
        

        