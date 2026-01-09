# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """

        Step 1 - Find deepest nodes (Maybe using BFS?)

        Step 2 - Once found, LCA for the 2 nodes

        BFS to determine levels, lowest level = deepest node

        Then dfs to find lowest common ancestor of both
        0
    1       3
null  2 

        I can find the LCA of the first deepeest node and last deepest node to get the answer

        Challenging part:
            1. After leaf nodes are stored in a list, I was struggling to understand how to select or process n leaf nodes for my upcoming function (findLowestCommonAncestor) 
            2. Figured out that my BFS will help store leaf nodes in L to R fashion, so all I need to do is selected the leftmost and rightmost leaf nodes and find the LowestCommonAncestor for those two
        """

        def isNumPresentInSubtree(num, node):
            if not node:
                return False

            if node.val == num:
                return True

            return isNumPresentInSubtree(num, node.left) or isNumPresentInSubtree(num, node.right)

        queue = deque()
        queue.append(root)
        copy = []
        level = 0   #holds the level at which deepest nodes are found
        while queue:
            copy1 = queue.copy()

            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not queue:
                copy = copy1
            if queue:
                level += 1
        
        print(copy)     #holds leaf nodes

        def findLca(node: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]):

            if not node:
                return None
            if node.val == p.val or node.val == q.val:
                return node

            L, R = findLca(node.left, p, q), findLca(node.right, p, q)

            if L and R:
                return node
            return L or R

        return findLca(root, copy[0], copy[-1])
        