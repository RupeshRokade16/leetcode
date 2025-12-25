# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        queue = collections.deque()
        queue.append(root)
        res = []

        while queue:
            qLength = len(queue)
            level = []
            for i in range(qLength):
                node = queue.popleft()

                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)

        final = []

        for arr in res:
            final.append(arr[-1])

        return final
