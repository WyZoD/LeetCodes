from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        tail = dummy

        while head and head.next:
            first = head
            second = head.next

            tail.next = second
            first.next = second.next
            second.next = first

            head = first.next
            tail = first

        return dummy.next
