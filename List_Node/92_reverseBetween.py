92_反转链表 II
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

时间复杂度
空间复杂度

总结:
1.p0.next = ... 等价于p0要指向谁， 而不是p1 = 什么
2.反转的结果就是p0（1）指向pre（4）， po.next（2）指向cur(5)
3.若left = 1， 就需要一个dummy node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        po = dummy
        for _ in range(left - 1):
            po = po.next
    
        pre = None
        cur = po.next
        for _ in range(right - left + 1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        po.next.next = cur
        po.next = pre
        return dummy.next