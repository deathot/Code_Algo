876_链表的中间结点

给你单链表的头结点 head ，请你找出并返回链表的中间结点。
如果有两个中间结点，则返回第二个中间结点。

时间复杂度
空间复杂度

总结:
1.数学归纳法——当fast或fast.next 为空时， slow就是中间节点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p0 = dummy
        cnt = 0
        cur = head
        
        while cur:
            cur = cur.next
            cnt += 1
        
        for _ in range(cnt // 2 + 1):
            p0 = p0.next
        
        return p0
 