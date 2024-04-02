'''
235_二叉搜索树的最近公共祖先

给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

空间复杂度o(n)

总结：
首先不用考虑root为空的情况， 因为是二叉搜索树， 且题目给出p， q在树中， （二叉搜索树， 左子树永远比右子树小）
1.分类讨论 一是 root是p 或 root是q 则返回root
          二是 判断p和q的值， 是否都大于root， 以及是否都小于root， 而后要么递归右子树， 要么递归左子树， 分别return
          三是 其余情况return root
2. if root > p or root > q != if root >p or q

'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root is p or root is q:
            return root
        
        x = root.val
        if x > p.val and x > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif x < p.val and x < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root



