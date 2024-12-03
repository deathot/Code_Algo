# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def midfunc(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reversefunc(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        mid = self.midfunc(head)
        head1 = self.reversefunc(mid)
        while head and head1:
            if head.val != head1.val:
                return False
            head = head.next
            head1 = head1.next
        return True
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode()
        copy = dummy
        cur = head
        
        while cur:
            copy.next = ListNode(cur.val)
            copy = copy.next
            cur = cur.next
        
        # Reverse the copied list
        prev, cur = None, dummy.next
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        # Compare the original and reversed copied list
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True