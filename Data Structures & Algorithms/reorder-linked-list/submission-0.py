# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return None

        node = head
        res = []
        while node:
            res.append(node.val)
            node = node.next
        
        l, r = 1, len(res) - 1
        i = 2
        start = head

        for j in range(len(res) - 1):

            if i % 2 == 0:
                head.next = ListNode(res[r])
                i += 1
                r -= 1
                head = head.next
            else:
                head.next = ListNode(res[l])
                i += 1
                l += 1 
                head = head.next
