142_环形链表 II

给定一个链表的头节点  head ，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。

不允许修改 链表。

时间复杂度o(n)
空间复杂度o(1)

总结:
1.结合图， 先判断是否为环， 若为环， 那么在最坏情况下， 当快慢指针相遇时，
慢指针也不会走超过环的距离。
# 2.    2(a + b) = a + b + k(b + c)
#       2a + 2b  = a + 2b + c + (k - 1)(b + c)
#       a - c = (k - 1)(b + c)
所以， 当快慢相遇时， head 和 slow 各走c步后， 再继续走， 终会在入口相遇， 此时返回slow即可
3.在链表中， 没有值， 不能有 == ， 只有位置， 返回的也是位置

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is slow:
                while slow is not head:
                    slow = slow.next
                    head = head.next
                return slow
        return None
        
  