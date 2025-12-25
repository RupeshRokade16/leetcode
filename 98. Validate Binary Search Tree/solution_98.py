# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        I need to pass seen limits downwards

        so a left limit and right limit

        For second example, at node 3
        The left limit should be 5, right limit should be 4

        The curr node's val should be
        1) Greater than left limit
        2) Less than right limit

        Say we start with -inf, 5, inf

        L = dfs(-inf, 5, min(right_limit, node.val))          -> Moving left changes right limit
        R = dfs(max(left_limit, node.val), 5, right_limit)


         2                          dfs(-inf, 2, inf) 
       1   3                        T and dfs(-inf, 1, 2) and dfs(2, 3, inf)

        """

        def dfs(left_limit, node, right_limit):  
            if not node:
                return True 

            flag = False

            if left_limit < node.val < right_limit:
                flag = True
            else:
                flag = False

            L = dfs(left_limit, node.left, min(right_limit, node.val))
            R = dfs(max(left_limit, node.val), node.right, right_limit)

            return flag and L and R

        return dfs(float('-inf'), root, float('inf'))
