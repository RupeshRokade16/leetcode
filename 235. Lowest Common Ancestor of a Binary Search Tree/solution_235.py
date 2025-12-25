# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        Think two scenarios - 1) 3 nodes, 2) (for basecase) leaf node
            O
        O       O

        The question we want to ask at each decision point is -
        Is p in left subhalf, is q in right subhalf (we know that p < q
        and p will exist in left and q in right for LCA condition
        
        Also, if q exists in right, p may exist on left or the curr node itself
        viceversa for p existing on left)

           5 
          3 8
        1 4 7 9
        say p = 3, q = 9
        dfs(root)
        We know 3 (p) < 5 < 9 (q)
        If it were 3 (p) < 4 (q) < 5
        

            so dfs called on left and right (stored in L and R)
                if node.val == p.val:
                return True
        """

        if not root:
            return
        if p.val > q.val:
            tmp = p
            p = q
            q = tmp

        res = [0]
        def dfs(node, p, q):
            if p.val < node.val < q.val:
                return node

            if p.val < q.val < node.val:
                #Move left
                return dfs(node.left, p, q)

            if node.val < p.val < q.val:
                #Move right
                return dfs(node.right, p, q)

            if p.val == node.val:
                return p

            if q.val == node.val:
                return q
            

        res = dfs(root, p, q)

        return res
