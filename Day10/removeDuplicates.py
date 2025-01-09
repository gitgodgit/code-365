class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
class Solution:
    def deleteDuplicates(self, head):
        last_node = head
        while(hasattr(last_node, "next") and last_node.next is not None):
            if last_node.val == last_node.next.val:
                last_node.next = last_node.next.next
            else:
                last_node = last_node.next
        return head