# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str_1 = ''
        str_2 = ''
        while l1:
            str_1 += str(l1.val)
            l1 = l1.next
        while l2:
            str_2 += str(l2.val)
            l2 = l2.next
        s1 = str_1[::-1]
        s2 = str_2[::-1]
        res = int(s1) + int(s2)
        res = str(res)
        print(res)
        dummy = ListNode()
        node = dummy
        for i in range(len(res) - 1, -1, -1):
            node.next = ListNode(res[i])
            node = node.next
        return dummy.next