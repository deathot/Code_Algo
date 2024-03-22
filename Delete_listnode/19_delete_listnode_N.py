19_删除链表的倒数第 N 个结点

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

时间复杂度o(n)
空间复杂度o(1)

总结:
1.需要一个dummynode， 如果链表只有一个节点的话
2.对于删除倒数第n个节点， 只需要知道倒数第n+1个节点即可
3.right先走n步， left和right在一起走， 直到right.next为空， left则为倒数第n+1个

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        right = dummy
        left = dummy
        for _ in range(n):
            right = right.next
        
        while right.next:
            left = left.next
            right = right.next
        
        left.next = left.next.next

        return dummy.next
        