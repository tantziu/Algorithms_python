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

    def add_to_list(self, head, node):
        if head is None:
            return node
        current = head
        while current.next:
            current = current.next
        current.next = node
        return head


    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # if l1 is None:
        #     return 
        result = ListNode()
        tail = result
        
        while l1 or l2:
            if l1 is None:
                tail.next = l2
                break
            if l2 is None:
                tail.next = l1
                break
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        return result.next





#  Input: 
# l1 = [1,2,4] 
# l2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Input: 
# l1 = []
# l2 = []
# Output: []

# Input: 
l1 = []
l2 = [0]
# Output: [0]
ll = Linked_List()
head1 = ll.construct_linked_list(l1)
head2 = ll.construct_linked_list(l2)
new_head = ll.mergeTwoLists(head1, head2)
ll.print_list(new_head)

