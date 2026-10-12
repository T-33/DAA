class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        curr = head
        arr = []
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        start, end = 0, len(arr) - 1
        while start <= end:
            print(start, end)
            if arr[start] != arr[end]:
                return False
            start += 1
            end -= 1
        return True