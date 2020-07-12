"""
给定一个二叉树，返回其节点值自底向上的层次遍历。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
例如：
给定二叉树 [3,9,20,null,null,15,7],

    3
   /
  9  20
    /  \
   15   7
返回其自底向上的层次遍历为：

[
  [15,7],
  [9,20],
  [3]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    node_list = []
    def depth_travel(self,root,depth=0):
        if not root:
            return self.node_list
        self.node_list.append([])
        self.node_list[depth].append(root.val)
        self.node_list.append([])
        self.depth_travel(root.left,depth+1)
        self.depth_travel(root.left,depth+1)
        self.depth_travel(root.right,depth+1)

    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.depth_travel(root,0)
        return self.node_list





