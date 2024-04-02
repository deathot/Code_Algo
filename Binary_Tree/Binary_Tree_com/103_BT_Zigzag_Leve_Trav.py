'''
103. 二叉树的锯齿形层序遍历

给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

空间复杂度o(n)

总结:
1.判断为空
2.用双端队列deque， 先从root开始， 遍历每一个node， 加到vals中而后把下一层node放入队列中，
直到deque为空， 最后vals 加到ans中
3.和102区别在于 要加一个even 判断当前层是否为奇或偶
从而加ans时， 是否正或倒

'''
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        ans = []
        q = deque([root])
        
        while q:
            vals = []
            for _ in range(len(q)):
                node = q.popleft()
                vals.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(vals)

        return ans