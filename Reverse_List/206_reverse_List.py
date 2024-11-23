206_反转链表

时间复杂度o(n)
空间复杂度o(1)

总结:
1.用递归处理， 修改的是指针
2.先记录当前节点的下一个节点， 再让当前节点的下一个节点的指针指向上一个元素，
然后更新上一个元素 等于下一个要处理的节点， 最后再让当前节点等于下一个节点
3.用迭代的话相当于没有cur.next = pre 这一行， 最后返回的是反转后的第一个元素， 并没有修改指针

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur != None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre  = None
        cur = head

        while cur != None:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre