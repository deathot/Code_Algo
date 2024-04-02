'''
102. 二叉树的层序遍历

给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
空间复杂度o(n)

总结:
1.判断为空
2.用双端队列deque， 先从root开始， 遍历每一个node， 加到vals中而后把下一层node放入队列中，
直到deque为空， 最后vals 加到ans中

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
