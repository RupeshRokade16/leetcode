# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        2,4,3 -> 3 4 2
        5,6,4 -> 4 6 5
        +
        7,0,8 -> 8 0 7

        Writing neetcode solution at the bottom
        """

        curr1, curr2 = l1, l2
        carry_over = 0
        dummy = ListNode()
        prev = dummy

        while curr1 and curr2:
            #Add 2 numbers with carryover
            total = curr1.val + curr2.val + carry_over
            addition = total - 10 if total >= 10 else total

            #Compute new carry_over
            carry_over = 1 if total >= 10 else 0

            new_node = ListNode(addition)
            prev.next = new_node
            prev = new_node

            curr1 = curr1.next
            curr2 = curr2.next

        if curr2 and not curr1:
            curr1 = curr2
        
        if curr1:
            while curr1:
                total = curr1.val + carry_over
                addition = total - 10 if total >= 10 else total

                carry_over = 1 if total >= 10 else 0

                new_node = ListNode(addition)
                prev.next = new_node
                prev = new_node

                curr1 = curr1.next
        
        if carry_over:
            prev.next = ListNode(carry_over)

        return dummy.next


        """
        dummy = ListNode()
        cur = dummy

        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            #new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            cur.next = ListNode(val)

            #update ptrs
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next
        """
