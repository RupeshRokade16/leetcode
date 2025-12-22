# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        [0,   1,   2,    3,    4,    5,    6]
        [0, n-1,   1,  n-2,    2,  n-3,    3]

        Initially I though keeping a head and tail ptr can solve
        But its better to rather
            find the mid point and and then move head and mid ptrs to the 
            right

        Thinking of reordering, 1st node pts to last node which pts to 2nd node
        and so on. Draw it on a paper

        We want split at half the length and reverse the second half of the list
        Then 2 ptrs at start of each list and then stitch up

        You can also use slow and fast ptr approach to jump till the pivot

        Wrote neetcode's solution as I was complexly calculating midpoint using
        math which made it off by 1
        """
        #Start at 0, 1
        slow, fast = head, head.next
        
        #Jump to 1, 3 as long as 1, 2 exist
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = None
        slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
                  