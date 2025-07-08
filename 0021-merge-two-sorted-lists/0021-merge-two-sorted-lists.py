# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merged_list = ListNode()      # Dummy head
        current = merged_list         # Pointer to build the list

        # Merge while both lists have nodes
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # Attach the rest of the non-empty list
        current.next = list1 if list1 else list2
        
        #remaining = list1 if list1 is not None else list2
        #while remaining is not None:
        #    current.next = ListNode(remaining.val)
        #    current = current.next
        #    remaining = remaining.next

        return merged_list.next  # Skip the dummy node