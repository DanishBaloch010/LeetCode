# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # head nahi hai ya ek node hai.
        if not head or not head.next:
            return head
        
        # odd pehla wala hai even uske agla wala (starting case)
        odd = head
        even = head.next

        # yaha par ek aur kaam hoga, wait for it.(done)
        even_head =  head.next

        while even and even.next:
            # odd ko ikhata karo
            odd.next  = even.next
            odd  = even.next

            # even ko ikhata karo
            even.next =  odd.next
            even = odd.next

            # just for understanding
            # current = current.next

        odd.next = even_head

        return head









        

        
        