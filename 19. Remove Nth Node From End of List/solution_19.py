# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Find length of list, say = 4
        Then you need to evict (4 - n + 1)th node from start
        See example
        """
        dummy = ListNode()
        prev, curr = dummy, head
        prev.next = curr

        length = 0
        #if not length: return head

        #Find length
        while curr:
            #count curr in length
            length += 1
            
            #traverse
            tmp = curr.next
            prev = curr
            curr = tmp
        
        node_idx = length - n + 1

        prev, curr = dummy, head
        curr_idx = 0
        while curr:
            #count curr in length
            curr_idx += 1

            if curr_idx == node_idx:
                #Remove curr node
                tmp = curr.next if curr else None
                prev.next = tmp
                break
            else:
                #Move ptrs
                tmp = curr.next
                prev = curr
                curr = tmp
        return dummy.next
