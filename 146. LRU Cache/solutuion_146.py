from collections import deque

"""
Need to keep a deque, with dummy nodes at both ends to enable popping
and rearrangement. We could keep the LRU always to the left most part
of the deque, and the MRU at the right most
So every get operation will pop the element and place to the right
end
And every put, will either update the value else add to right most if 
it doesnt exist else pop and add.

Might need a hashmap to track what exists in the cache and what doesnt
Deque for O(1) get and put operations

Writing my own deque as I need each element to be doubly linked and
I want control over those elements

So to summarize, created a doubly linked list, with key and value in 
each node. Every key will also be stored in a dictionary for fast 
retrieval

Was getting an error due to my custom counting, instead rely on len
of dict function"""

class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {} #key -> Node

        #Create dummies, link to each other
        self.Left, self.Right = Node(), Node()
        self.Left.next = self.Right
        self.Right.prev = self.Left

        self.total_capacity = capacity


    def get(self, key: int) -> int:
        if key in self.cache:
            #Convert to MRU
            self.remove(self.cache[key]) #Remove Node
            self.add(self.cache[key]) #Add Node
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #Remove node
        
        #Create new 
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.add(newNode)

        if len(self.cache) > self.total_capacity:
            lru = self.Left.next
            self.remove(lru)
            del self.cache[lru.key]

    def remove(self, node):
        prv, nxt = node.prev, node.next
        prv.next, nxt.prev = nxt, prv

    def add(self, node):
        prv, nxt = self.Right.prev, self.Right
        prv.next = nxt.prev = node
        node.prev, node.next = prv, nxt
        
"""
    LEFT_DUMMY  O    O    RIGHT_DUMMY

    {dict holding values inside LRU and their memory locations at the deque

    Leftwards -> Least recently used
    Rightwards -> Most Recently used

    Helper functions:
    Remove Node (No location needed)
    Add Node to Right (Always added to the right)

    Extra things: 
    You remove a node when
        1) Capacity full -> find lru, delete node, del from dictionary
        2) YOu get a node (Makes it mru), so delete node, add a new node with key and new value, update dictionary with key and node location
"""
