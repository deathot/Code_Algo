98_Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

时空复杂度:o(n)

总结:
1.后序遍历: left, right, root
            1).要把每个节点的左子树最小与最大值， 右子树的最小最大值都记录下来
            2).最后返回的是某个节点左子树的最小值与右子树的最大值。
            3).在以上1， 2的嵌套下， 比如说某个节点是右子树的左子树， 那么这时候这个右子树的最小值就能和它底下的左子树的最大值进行比较
也就是后续的if语句如果 if x <= l_max or x >= r_min:
                return -inf, inf

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(node):
            if node is None:
                return inf, -inf
            l_min, l_max = f(node.left)
            r_min, r_max = f(node.right)
            x = node.val
            if x <= l_max or x >= r_min:
                return -inf, inf
            return min(l_min, x), max(r_max, x)
        return f(root)[0] != -inf
            
2.中序遍历: left, root, right
        1).相当于先把所以节点从小到大排序， 在判断相邻值是否符合大小
        2).要为第一个排序的第一个值给一个前置条件值即为-inf
        3).对于if not self.isValidBST(root.left): 意思是调用主函数， 如果他不是二叉搜索树直接返回false
        4).先判断左子树是否为有效的依据是下面的 if root.val <= self.pre:， 再判断递归右子树

class Solution:
    #Mid
    pre = -inf
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        if not self.isValidBST(root.left):
            return False
        if root.val <= self.pre:
            return False
        self.pre = root.val
        return self.isValidBST(root.right)
            
3.先序遍历: root, left, right
        1).思想是判断当前节点值是否符合范围， 而后先递归左子树， 并修改下个一个节点的右边界， 最后递归右子树， 修改左边界

class Solution:
    #Pre
    def isValidBST(self, root: Optional[TreeNode], left= -inf, right= inf) -> bool:
        if root is None:
            return True
        x = root.val
        return left < x < right and self.isValidBST(root.left, left, x) and self.isValidBST(root.right, x, right)