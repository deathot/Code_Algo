143_重排链表

示例：
    输入：head = [1,2,3,4]
    输出：[1,4,2,3]

时间复杂度:o(n)
空间复杂度:o(1)

总结:
1.翻转列表的作用是，获得退出循环的条件
2.末尾节点总是先插入， 所以先处理末尾节点

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
        

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur != None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def reorderList(self, head: Optional[ListNode]) -> None:
       mid = self.middleNode(head)
       head2 = self.reverseList(mid)
       while head2.next:
        nxt = head.next
        nxt2 = head2.next
        head.next = head2
        head2.next = nxt
        head = nxt
        head2 = nxt2

       