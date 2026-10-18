# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        if head is None or head.next is None:
            return head

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        curr = head
        while curr:
            if curr.next is mid:
                curr.next = None
                break
            curr = curr.next

        left = self.sortList(head)
        right = self.sortList(mid)

        return self.mergeTwoLists(left, right)

    # Merges two sorted lists into a sorted list
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2