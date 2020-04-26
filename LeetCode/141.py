# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """


        def solve(head):
            head.val = -10 ** 10
            if head.next is None:
                return False
            elif head.val == -10 ** 10:
                return True
            else:
                solve(head.next)

        return solve(head)