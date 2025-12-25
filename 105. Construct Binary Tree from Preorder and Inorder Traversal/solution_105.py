# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Preorder [ 3, 9, 20, 15, 7]
        Inorder= [9, 3, 15, 20, 7]
        1st value will always be root in preorder

        from the remaining values, we want to know which go in the left subtree
        and right subtree

        that's when we use inorder array
        find root in inorder (index 1)
        that tells us that every value to left is gonna go in the left subtree and
        every value to the right is gonna go in the right subtree
        1 value in left subtree and 3 values in right subtree

        Then use that, partition array of preorder using this info [9] [20, 15, 7]

        Then next value in paritioned array gives the new node, then find it inorder
        traversal (index will be called mid), find how many values to the left and right 
        (also remove from both arrays once consumed)
        """

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0]) #index locating curr node in inorder

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid]) #skip 0th index as it consumed, and mid used for num of elements
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
        