141_环形链表

给你一个链表的头节点 head ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。

如果链表中存在环 ，则返回 true 。 否则，返回 false 。

时间复杂度o(n)
空间复杂度o(1)

总结:
1.快指针相当于比慢指针每次都多走一步，
如果有环， 快指针就会 = 慢指针
2.退出循环的条件， 如果有环， 循环内return
否则， 在循环内else的话，直接就flase， 因为循环第一步就 ！=

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
            
        return False
        
        