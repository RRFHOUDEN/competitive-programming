# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        if root.left is None and root.right is None:
            return True

        if not (root.left is None):
            if not Solution.isValidBST(self, root.left):
                return False

        if not (root.right is None):
            if not Solution.isValidBST(self, root.right):
                return False

        ans = True

        if not (root.left is None):
            if root.val > root.left.val:
                ans = True
            else:
                ans = False

        if not (root.right is None):
            if root.val < root.right.val:
                return ans * True
            else:
                return ans * False

        return ans