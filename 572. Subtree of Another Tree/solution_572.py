# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        """ 
        Keep traversing till you reach the end of the root
        If you find the first common point, only then run the isSameTree function

        Look at the optimal solution where they do it in O(m+n) for both space and time
        """
        if not subRoot: return True
        if not root: return False

        def isSameTree(p, q):

            if not p and not q:
                return True

            if p and q and p.val == q.val:
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

            else:
                return False

        #If p goes out of bounds
        if not root:
            return False

        attempt = False
        if root.val == subRoot.val:
            attempt = isSameTree(root, subRoot)
            if attempt:
                return True

        L = self.isSubtree(root.left, subRoot)
        R = self.isSubtree(root.right, subRoot)

        return attempt or L or R
