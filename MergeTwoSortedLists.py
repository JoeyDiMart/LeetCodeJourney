# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def mergeTwoLists(self, list1, list2):
        def add(list, Node):
            pass

        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        merged_lists = ListNode()

        if list1 is None and list2 is None:
            return []
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        while True:
            if list1.val is None:
                if list2.val is None:
                    return merged_lists
                else:
                    add(merged_lists, list2.val)
                    continue
            elif list2.val is None:
                add(merged_lists, list1.val)
                continue

            if list1.val <= list2.val:
                add(merged_lists, list1.val)
