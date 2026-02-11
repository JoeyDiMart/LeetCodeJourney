# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        def add(merged_lists, Node):
            pass

        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merged_lists = ListNode()

        if list1 == None and list2 == None:
            return []
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1

        while True:
            if list1.val == None:
                if list2.val == None:
                    return merged_lists
                else:
                    add(merged_lists, list2.val)
                    continue
            elif list2.val == None:
                add(merged_lists, list1.val)
                continue

            if list1.val <= list2(list2_point).val:
                add(merged_lists, list1.val)
