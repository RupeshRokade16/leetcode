"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Right off the bat, I'm thinking of creating a list with elements as
        nodes
        This was my head would correspond to 0th index

        [[3,null],   [7,3],      [4,0],      [5,1]     ] -> Here the 1st element is
        the .val, and second element is the .random which is actually an index of
        the node it is pointing to.

        [ListNode(), ListNode(), ListNode(), ListNode()]

        As I traverse, 
        ListNode(.random = Null), ListNode(.random = arr[3]), ListNode(.random = arr[0]), ListNode(.random = arr[1])]

        This is only possible since I created the result arr in the list format
        Which gives me access to future indices before creation

        The question is wrong in saying it is an index for the random_index
        whereas it is actually pointing to random_node - This changes the
        logic heavily

        Will place the input into an arr sequentially.
        Then go through the arr and create a map of element -> index. (Needed for .random)
        Then build res array using these 2 pieces of info

        READ SPACE OPTIMIZED SOLUTION OF NEETCODE - V good
        """
        #Edge Case
        if not head: return 

        curr = head
        ref1 = []

        while curr:
            ref1.append(curr)
            curr = curr.next

        elementIdxMap = {}
        ref2 = []

        for i, node in enumerate(ref1):
            #Create a new node to store in result array
            new_node = Node(node.val)
            ref2.append(new_node)

            elementIdxMap[node] = i #Store each node's index location
            #mem -> idx
        
        for i, node in enumerate(ref1):
            curr = ref2[i]
            
            curr.next = ref2[elementIdxMap[node.next]] if node.next else None
            curr.random = ref2[elementIdxMap[node.random]] if node.random else None

        return ref2[0]
