import math
class Solution(object):
    def deleteMiddle(self, head):

        if not head or not head.next:
            return None

        count = 0
        temp = head

        while temp:
            count += 1 
            temp = temp.next


        mid = count // 2

        i = 0 
        prev = None
        current = head 
        while i < mid:
            prev = current
            current = current.next 
            i += 1
        
        prev .next = current.next
        return head