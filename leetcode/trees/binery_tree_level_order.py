class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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
    
    def traverse_levels(self, root):
        if not root:
            return []
        level_list = []
        temp_list = []
        result = []
        node = root
        level_list.append(node)

        while level_list:
            result.append(list(map(lambda x: x.val, level_list)))

            for element in level_list:
                if element.left is not None:
                    temp_list.append(element.left)
                if element.right is not None:
                    temp_list.append(element.right)
            
            
            level_list = temp_list
            temp_list = []

        return result


# tree_elements = [3,9,20,None,None,15,7]
# tree_elements = [1]
tree_elements = []
s = Solution()
root = s.construct_tree(tree_elements)
print(s.traverse_levels(root))