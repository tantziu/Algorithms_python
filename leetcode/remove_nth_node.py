# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None

    def construct_linked_list(self, a):
        node = dummy =  ListNode()
        for i in a:
            node.next= ListNode(i) 
            node = node.next
        return dummy.next


    def print_list(self, node):
        value = node
        while value:
            print(value.val, end = ' ')
            value = value.next


    def removeNthFromEnd(self, head: ListNode, n: int):
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        # print("length: ", length)

        if length == n:
            return None

        remove_index = length - n
        node = dummy
        while remove_index > 0:
            if node.next:
                remove_index -= 1
                node = node.next
        
        node.next = node.next.next
        return dummy.next

a = [1,2,3,4,5]
n = 2
# Output: [1,2,3,5]
# ---------------
# a = [1]
# n = 1
# Output: []
# --------------
# a = [1,2] 
# n = 1
# Output: [1]
# --------------
ll = Linked_List()
head = ll.construct_linked_list(a)
# ll.print_list(head)
ll.removeNthFromEnd(head, n).val
ll.print_list(head)