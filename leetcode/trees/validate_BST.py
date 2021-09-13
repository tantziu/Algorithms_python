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

    
    def traverse_dfs(self, root):
        stack = []
        node = root
        # visited = []
        stack.append(node)
        while stack:    
            node = stack.pop()

            print(node.val)
            # if node not in visited:
            #     visited.append(node)

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def traverse_bfs(self, root):
        queue = []
        node = root
        queue.append(node)
        while queue:    
            node = queue.pop(0)

            print(node.val)
            # if node not in visited:
            #     visited.append(node)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    def traverse_bfs_depth(self, root):
        queue = []
        node = root
        queue.append(node)
        levels = 0
        while queue: 
            tmp_queue = []
            for node in queue:  
                print(node.val) 
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            print()
            queue = tmp_queue    

            levels += 1
        return levels


    def traverse_dfs_recursive(self, root):
        if not root:
            return
        
        print(root.val)
        self.traverse_dfs_recursive(root.left)
        self.traverse_dfs_recursive(root.right)
                
            
 
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
            return

        self.visited_node = None
        self.is_valid = True
        self.in_order_traversal(root)

        return self.is_valid

    
    def in_order_traversal(self, root):
        if root:
            self.in_order_traversal(root.left)
            
            print(root.val)
            if self.visited_node is not None and root.val <= self.visited_node:
                self.is_valid = False
            self.visited_node = root.val

            self.in_order_traversal(root.right)
    

# tree_elements = [3,9,20,None,None,15,7]

# tree_elements = [5,1,4,None,None,3,6]
# tree_elements = [2, 1, 3]
tree_elements = [2, 2, 2]
s = Solution()
root = s.construct_tree(tree_elements)
# print(s.traverse_dfs_recursive(root))
# s.in_order_traversal(root)
print(s.validate(root))


