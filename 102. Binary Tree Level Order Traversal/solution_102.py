# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        queue = deque()

        queue.append((root,0))  # (node, level)

        res = [[]]      #index -> 0 will contain level = 0
                        #index -> 1 will contain level = 1

        while queue:

            node, level = queue.popleft()

            L, R = node.left, node.right

            if L:
                queue.append((L, level+1))
            if R:
                queue.append((R, level+1))


            if level == len(res):
                res.append([])
            res[level].append(node.val)

        return res

        """Alt solution by neetcode:
            res = []

            queue = collections.deque()
            queue.append(root)

            while queue:
                qLength = len(queue)    #len of current queue (makes it level wise)
                level = []

                for i in range(qLength):
                    node = q.popLeft()
                    if node:
                        level.append(node.val)
                        q.append(node.left)
                        q.append(node.right)
                if level:
                    res.append(level)

                return res
        """
