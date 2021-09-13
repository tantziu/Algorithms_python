class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        left_data = self.left.data if self.left else None
        right_data = self.right.data if self.right else None
        out = [f"{self.data}: {left_data} {right_data}"]
        if self.left:
            out.append(str(self.left))
        if self.right:
            out.append(self.right.__repr__())

        return "\n".join(out)


# root = TreeNode("1")
# root.left = TreeNode("2")
# root.right = TreeNode("3")
# root.left.left = TreeNode("4")
# root.left.right = TreeNode("5")
# root.right.right = TreeNode("6")
#
# print(root)

