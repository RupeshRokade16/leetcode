# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and not q: return True

        # if p and not q: return False

        # if q and not p: return False

        # if p.val != q.val: return False       # can instead write the converse

        if p and q and p.val == q.val:
            
            L, R = self.isSameTree(p.left, q.left), self.isSameTree(p.right, q.right)

            return L and R

        else:
            return False
