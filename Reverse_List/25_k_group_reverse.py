25_K个一组翻转链表

给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。

k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

时间复杂度
空间复杂度

总结:
1.先分解思考 - 每一组都是组内翻转， 而后再拼接下一组， 更新p0， 再翻转下一组
2.每组， 组内cycle k次， 而后指针改变方向， 再去拼接， 所以先记录新p0，
再拼接 1 -> 3, p0 -> 2, 至此变为21345， 更新p0， 翻转下一组
3.初始化一个dummy_node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        dummy = ListNode(next = head)
        p0 = dummy
        
        pre = None
        cur = p0.next
        while n >= k:
            n -= k
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            nxt = p0.next
            p0.next.next = cur
            p0.next = pre
            p0 = nxt
        
        return dummy.next
        