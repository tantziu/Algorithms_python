# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
    def delete_node(self, node):
        temp = node.next
        node.val = temp.val
        node.next = temp.next


    def construct_linked_list(self, a):
        node = dummy =  ListNode(0)
        for i in a:
            node.next= ListNode(i) 
            node = node.next
        return dummy.next


    def print_list(self, node):
        value = node
        while value is not None:
            print(value.val, end = ' ')
            value = value.next
    

# Input: head1 = [4,5,1,9], node1 = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.

head2 = [4,5,1,9]
node2 = 1
# ---------------------
head3 = [1,2,3,4]
node3 = 3
# ---------------------
head4 = [0,1]
node4 = 0
# ---------------------
head5 = [-3,5,-99]
node5 = -3
# --------------

# linked_list = ListNode(4)
# e2 = ListNode(5)
# e3 = ListNode(1)
# e4 = ListNode(9)
# linked_list.next = e2
# linked_list.next.next = e3
# linked_list.next.next.next = e4
solution = Solution()
# solution.print_list(linked_list)
# solution.delete_node(e2)
# solution.print_list(linked_list)

head_result = solution.construct_linked_list(head3)
solution.print_list(head_result)
# solution.delete_node(ListNode(node3))
# solution.print_list(head_result)


