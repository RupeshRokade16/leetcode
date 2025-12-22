# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        prev, curr1, curr2 = dummy, list1, list2

        while prev:

            if curr1 and curr2:
                if curr1.val <= curr2.val:
                    temp = curr1.next
                    prev.next = curr1
                    prev = curr1
                    curr1 = temp
                else:
                    temp = curr2.next
                    prev.next = curr2
                    prev = curr2
                    curr2 = temp
            elif curr1:
                prev.next = curr1
                prev = False
            else:
                prev.next = curr2
                prev = False

        return dummy.next
                    