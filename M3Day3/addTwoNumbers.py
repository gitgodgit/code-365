class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reminder = 0
        l3 = ListNode(0)

        while not (l1 or l2):
            if l1 != None:
                int1 = l1.val
            else:
                int1 = 0
            if l2 != None:
                int2 = l2.val
            else:
                int2 = 0
            summery = int1 + int2 + reminder
            reminder = summery // 10
            l3.next = ListNode(summery % 10)
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
            l3 = l3.next
        if reminder:
            l3.next = ListNode(reminder)
        return l3.next

