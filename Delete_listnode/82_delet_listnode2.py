82_删除排序链表中的重复元素 II

给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 

时间复杂度o(n)
空间复杂度o(1)

总结:
1.需要一个dummynode， 若第0个节点就是重复元素的话
2.对于删除， while遍历所有节点， 先记录当前节点val， 而后再if判断当前节点的下下个节点val是否一致， 若一致， 再while循环判断， 当前节点的下一个节点存在并且值==val， 最后删除
而后cur遍历
3.2 while， 1 if

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next = head)
        cur = dummy
        
        while cur.next and cur.next.next:
            val = cur.next.val
            if cur.next.next.val == val:
                while cur.next and cur.next.val == val:
                        cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next