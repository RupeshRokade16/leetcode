# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""I have a dummy node connected before head, starting slow at dummy
and fast at dummy.next. The problem comes at the movement step where
fast.next or fast.next.next can be null. I added that into an if block
and I am returning false for such ifs, else moving my fast
This solution however would be make it difficult to find the index 
at which the circle repeats."""

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        dummy.next = head

        slow, fast = dummy, dummy.next

        while slow and fast:
            #Breaking condition
            print(slow.val, fast.val)
            if slow and fast and slow == fast:
                return True

            #Movement
            slow = slow.next
            if not fast.next or not fast.next.next:
                return False
            else:
                fast = fast.next.next
        return False
    