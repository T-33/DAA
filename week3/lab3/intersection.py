class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        visitedA = set()
        visitedB = set()


        currA = headA
        currB = headB

        while currA:
            visitedA.add(currA)
            currA = currA.next
        
        while currB:
            if currB in visitedA:
                print(currB)
                return currB
            currB = currB.next
        return None


##2 Second solution that I didnt come up with, but understood the concept

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        curr1 = headA
        curr2 = headB

        while curr1 != curr2:
            curr1 = curr1.next if curr1 else headB
            curr2 = curr2.next if curr2 else headA
        return curr1