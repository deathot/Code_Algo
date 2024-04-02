110_平衡二叉树

给定一个二叉树，判断它是否是 
平衡二叉树
  
时空复杂度o(n)

总结:
1.先判断左右子树是否是平衡子树
2.在判断左右子树相差深度是否超过1
3.判断平衡的条件是abs（left - right）> 1这句, 如果成立那么对于当前节点返回-1， 并一路返回到相对顶部

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node):
            if node is None:
                return 0
            left_he = get_height(node.left)
            if left_he == -1:
                return -1
            right_he = get_height(node.right)
            if right_he == -1 or abs(left_he - right_he) > 1:
                return -1
            return max(left_he, right_he) + 1
        return get_height(root) != -1
            