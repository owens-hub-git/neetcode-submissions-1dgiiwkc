# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 0:
            return head
        res = []
        node = head
        
        while node:
            res.append(node.val)
            node = node.next
        
        remove_node = len(res) - n
        res.pop(remove_node)

        d = ListNode()
        new_list = d

        for i in res:
            new_list.next = ListNode(i)
            new_list = new_list.next

        return d.next