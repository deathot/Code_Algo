104_二叉树的最大深度

给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

时间复杂度o(n)
空间复杂度o(n)

总结:
1.递归调用自身函数， 将最大值保存， 最后获得答案
2.此题递归调用并保存类似栈， 后进先出， 所以最坏情况空间复杂度占用o(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def f(node, cnt):
            if node is None:
                return
            cnt += 1
            nonlocal ans
            ans = max(ans, cnt)
            f(node.left, cnt)
            f(node.right, cnt)
        f(root, 0)
        return ans
                    
        