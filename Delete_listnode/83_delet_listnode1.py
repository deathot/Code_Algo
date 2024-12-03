83_删除排序链表中的重复元素

给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。

时间复杂度o(n)
空间复杂度o(1)

总结:
1.不需要dummynode， 因为最坏情况也是删除第1一个节点
2.遍历所有节点

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        cur = head

        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head == None:
            return head
        cur = head
        while cur.next:
            if cur.next.val == cur.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head