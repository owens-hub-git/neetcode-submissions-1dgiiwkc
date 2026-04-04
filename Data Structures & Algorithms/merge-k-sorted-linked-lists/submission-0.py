# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged_arr = []
        for i in lists:
            while i:
                merged_arr.append(i.val)
                i = i.next

        merged_arr.sort()

        d = ListNode()
        node = d
        for i in merged_arr:
            node.next = ListNode(i)
            node = node.next
        return d.next
