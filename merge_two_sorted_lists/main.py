# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
    def __str__(self):
        # return "ListNode{val: " + f"{self.val}" + ", next: " + f"{self.next}"+  "}"
        return f"{self.val}{f",{self.next}" if self.next != None else ""}"


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        head = ListNode(0)
        current_node = head

        while list1 and list2 :
            if list1.val <= list2.val:
                current_node.next = list1
                list1 = list1.next
            else:
                current_node.next = list2
                list2 = list2.next
            current_node = current_node.next

        current_node.next = list1 if list1 else list2

        return head.next
        

x1 = ListNode(val=1,next = ListNode(val=2,next = ListNode(val=4)))
y1 = ListNode(val=1,next = ListNode(val=3,next = ListNode(val=4)))
x2 = None
y2 = None
x3 = None
y3 = ListNode(val=0)

s = Solution()
n = [[x1,y1], [x2,y2], [x3,y3]]
for i in n :
    print(f"Merge [{i[0]}] and [{i[1]}] is equal to [{s.mergeTwoLists(i[0],i[1])}]")