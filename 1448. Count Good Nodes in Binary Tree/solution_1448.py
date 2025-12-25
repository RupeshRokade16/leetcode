# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Propagate the maximum value in a path

        As we go down the path from root, we need to carry the max till the path
        Here I am thinking more of root to node rather than leaf nodes propagated
        upwards

        Imagine leaf node condition:

                4
              1.   5
        
        return 0 for null
        return 
        """

        if not root:
            return 0

        def dfs(node, last_max):

            if not node:
                return 0

            count = 1 if last_max <= node.val else 0

            #Compute last max and traverse left and right
            L, R = dfs(node.left, max(last_max, node.val)), dfs(node.right, max(last_max, node.val))

            return count + L + R
        
        res = dfs(root, root.val)

        return res
