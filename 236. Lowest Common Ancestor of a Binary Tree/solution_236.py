# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        T: O(n), M: O(n)

        Thinking dfs,
            if we reach OOB
                return None
            if we find one of the two values
                we return the node at which we found one of the 2 values
                (calling it from root helps return root as answer if one of the
                2 values are root val)

            Next,
                We traverse L and R subtrees and store them as L and R

            If L and R both non null (meaning we found p and q (or q and p) in L and R),
                then we can confidently return the current node whose left and right children hold these values

            If one is null, the other holds the result (as it is propagated upwards from our second if block)
        """
        
        if not root:
            return None
        if root == p or root == q:
            return root

        L, R = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)

        if L and R:     #L and R are both not Null, meaning p and q found in diff subtrees
            return root
        
        return L or R   #One of the two is Null, we return the non null
