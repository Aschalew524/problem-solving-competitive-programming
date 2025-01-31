# Problem: Populating Next Right Pointers in Each Node - https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        left_most = root
        
        while left_most.left:
            cur = left_most
            
            while cur:
                cur.left.next = cur.right
                
                if cur.next:
                    cur.right.next = cur.next.left
                
                cur = cur.next
            
            left_most = left_most.left
        
        return root
        