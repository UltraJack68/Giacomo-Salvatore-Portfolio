"""Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well."""

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer = head
    
        while pointer and pointer.next:
            while pointer.next and pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
            pointer = pointer.next

        return head

