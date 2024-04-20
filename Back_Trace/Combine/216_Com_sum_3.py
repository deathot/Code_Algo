'''
216. 组合总和 III

找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
只使用数字1到9
每个数字 最多使用一次 
返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。

Tc:O(k*C(9, k))
Sc:O(k)

Summarize:
    Method1:选或不选
        1.边界条件为 d == 0时， 即path满时， 减枝思路为t < 0 或 n项和还是 < t
        2.递归所需参数需要一个t， 来判断是否加入ans

    Method2:枚举下一个要选的
        pass
        
'''