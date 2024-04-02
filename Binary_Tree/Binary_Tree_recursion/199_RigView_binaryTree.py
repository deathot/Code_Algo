'''
199_二叉树的右视图

给定一个二叉树的 根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

时空复杂度o(n)

总结：
1.因为最右边节点看到就可以加入，先递归右子树， 判断深度和ans长度是否一致，  一致则可加入
2.当右边子树递归完， len(ans)也被占用完， 剩下的就是递归左子树

'''
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def f(node, depth):
            if node is None:
                return 
            if len(ans) == depth:
                ans.append(node.val)
            f(node.right, depth + 1)
            f(node.left, depth + 1)
        f(root, 0)
        return ans
