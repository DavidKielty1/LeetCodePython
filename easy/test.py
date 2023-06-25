class ListNode:
        def __init__(self, val = 0, next = None):
            self.val = val
            self.next = next

class SLinkedList:
   def __init__(self):
      self.headval = None

list1 = SLinkedList()
list1.val = ListNode(1)
e2 = ListNode(2)
e3 = ListNode(4)

list2 = SLinkedList()
list2.val = ListNode(1)
f2 = ListNode(3)
f3 = ListNode(4)

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                tail = list1
                list1 = list1.next
            else:
                tail = list2
                list2 = list2.next
            tail = tail.next

        if list1:
             tail.next = list1
        elif list2:
             tail.next = list2

        return dummy.next
    
    mergeTwoLists(self='self', list1 = list1, list2 = list2)