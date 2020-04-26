# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):

        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        print(root)
        if root is None:
            return False
        if not(root.left is None):
            if Solution.hasPathSum(self, root.left, sum - root.val):
                return True
        if not(root.right is None):
            if Solution.hasPathSum(self, root.right, sum - root.val):
                return True
        if sum - root.val == 0 and root.right is None and root.left is None:
            return True
        else:
            return False