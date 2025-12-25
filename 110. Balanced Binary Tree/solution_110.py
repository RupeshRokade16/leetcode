# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        We want to find height of Left subtree and Right subtree

        Alternative soln in comments
        """
        res = True
        def dfs(node):
            nonlocal res

            if not node:
                return 0
                #return [True, 0]

            L = dfs(node.left)
            R = dfs(node.right)

            
            height_diff = abs(L - R)
            if height_diff > 1:
                res = False
            #balanced = L[0] and R[0] and abs(L[1] - R[1]) <= 1  #(alt to heigh_diff)

            #Send height upward
            return 1 + max(L, R)
            #return [balanced, 1 + max(L[1], R[1])]

        dfs(root)

        #return dfs(root)[0]
        return res
