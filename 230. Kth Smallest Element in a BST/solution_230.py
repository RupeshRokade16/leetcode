# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        kth smallest index

        Traversing and making an array, or marking the nodes
        Then finding the kth smallest number?

        storing in an array is fine but you can actually just keep 
        traversing in a dfs manner, while maintaing a count variable

        Traverse such that first element on the leftmost leaf is count == 1

        InOrder traversal to visit the tree in a sorted manner

        count variable helps count the indexes uptill now
        res variable will hold our result

        if self.result is not None helps exit out of the condition faster

        I also do not need to store the result of L and R here, since my code updates
        the nonlocal variable count and res upon visiting a node

        """

        count, res = 0, 0

        def dfs(node):
            nonlocal count, res

            if not node or res:
                return

            #Recrusively travel to the left         
            dfs(node.left)
            
            count += 1
            if count == k:
                res = node.val
                return

            #Lastly process right
            dfs(node.right)

        dfs(root)
        return res
