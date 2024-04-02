101_对称二叉树

给你一个二叉树的根节点 root ， 检查它是否轴对称。

时空复杂度o(n)

总结:
1.创建两个节点p, q 分别指向左右子树， 递归调用来判断是否轴对称

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def issametree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> int:
        if p is None or q is None:
            return p is q
        return p.val == q.val and self.issametree(p.left, q.right) and self.issametree(p.right, q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.issametree(root.left, root.right)