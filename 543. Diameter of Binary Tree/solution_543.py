# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0] #Couldnt do res as a var since it cant be accessed, inside dfs
        #res = 0       #Commenting the way to use a variable
        def dfs(node):
            #nonlocal res       #You declare it as non local here
            if not node:
                return 0

            L = dfs(node.left) #2
            R = dfs(node.right) #1

            #Calculate the number of edges (not nodes)

            """
            At any point, the number of edges, sum of edges to the left
            and edges to the right
            """

            res[0] = max(res[0], L + R)

            #Compute edge first
            total = 1 + max(L, R)

            return total

        dfs(root)
        return res[0]
