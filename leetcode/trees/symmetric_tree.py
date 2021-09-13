# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.visited_node = None
        self.is_valid = True
        self.half_tree = []
                
    
    def construct_tree(self, tree_list):
        if not tree_list:
            return None
        root = TreeNode(tree_list[0])
        queue = [root]
        i = 0
        while queue:
            node = queue.pop(0)
            if i+1 < len(tree_list) and tree_list[i+1]:
                node.left = TreeNode(tree_list[i+1])
                queue.append(node.left)
            if i+2 < len(tree_list) and tree_list[i+2]:
                node.right = TreeNode(tree_list[i+2])
                queue.append(node.right)
            i += 2
        return root
    

    def validate(self, root):
        if not root:
            return False

        # self.is_valid = True
        # self.in_order_traversal(root.left)
        return self.is_mirror(root.left, root.right)

    
    def is_mirror(self, root_left, root_right):
        if root_left is None and root_right is None:
            return True
        
        if root_left is None or root_right is None:
            return False

        return (root_left.val == root_right.val and
            self.is_mirror(root_left.left, root_right.right) and 
            self.is_mirror(root_left.right, root_right.left))

tree_elements = [1,2,2,None,3,None,3]
# tree_elements = [1,2,2,3,4,4,3]
s = Solution()
root = s.construct_tree(tree_elements)
# print(s.traverse_dfs_recursive(root))
# s.in_order_traversal(root)
print(s.validate(root))


