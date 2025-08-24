"""Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node."""

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
         
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        if fast.next:
            return slow.next
        
        return slow