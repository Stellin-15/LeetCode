class Solution(object):
    def pairSum(self, head):
        # 1) find middle (slow ends at start of second half for even length)
        slow, fast = head , head 

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        # 2) reverse second half starting at slow
        prev = None 
        current = slow 

        while current:

            nxt = current.next
            current.next = prev 
            prev = current 
            current = nxt 
        second_head = prev 
         # 3) compute twin sums
        max_sum = 0
        first_head = head 
        while second_head:
            max_sum = max(max_sum, first_head.val + second_head.val)
            first_head = first_head.next 
            second_head = second_head.next
        
        return max_sum


# another way to do it is to store all values in an array and then compute the max sum
class Solution(object):
    def pairSum(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        n = len(vals)
        ans = 0
        for i in range(n // 2):
            ans = max(ans, vals[i] + vals[n - 1 - i])
        return ans