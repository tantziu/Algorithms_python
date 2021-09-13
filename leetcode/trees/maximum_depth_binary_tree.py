# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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

    # def max_depth_no_recursion(self, root):
    #     if root is None:
    #         return 0

    #     max_depth = 0
    #     depth = 0

    #     visited = set()
    #     stack = []
    #     node = root
    #     stack.append(node)
    #     while stack:    
    #         node = stack.pop()
    #         visited.add(node)
    #         depth += 1

    #         if depth > max_depth:
    #             max_depth = depth

    #         if node.right:
    #             stack.append(node.right)

    #         if node.left:
    #             stack.append(node.left)
            
    #         if (node.left is None and node.right is None):
    #             depth -= 1
            
    #     return max_depth
                
            
 
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
    

    def maxDepth(self, root: TreeNode):
        if root is None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
        
        # print("LD", left_depth)
        # print("RD", right_depth)
        return max(left_depth, right_depth) + 1

# tree_elements = [3,9,20,None,None,15,7]
# tree_elements = [1,None,2]
# tree_elements = []
# tree_elements = [0]
tree_elements = [1,2,3,4,None,None,5]
s = Solution()
root = s.construct_tree(tree_elements)
# print(s.maxDepth(root))
print(s.traverse_dfs_recursive(root))
# print(s.max_depth_no_recursion(root))

# Input: root = [3,9,20,null,null,15,7]
# Output: 3
