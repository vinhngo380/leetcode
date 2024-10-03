class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        multiplier = 1
        num1, num2 = 0, 0
        while l1 is not None: # TC O(n)
            num1 += l1.val * multiplier
            multiplier *= 10
            l1 = l1.next
        multiplier = 1
        while l2 is not None: # TC O(m)
            num2 += l2.val * multiplier
            multiplier *= 10
            l2 = l2.next
        
        total = num1 + num2

        # get digits
        stack = [] 
        while total >= 0: # >= to allow for only 0 to be added
            stack.append(total % 10)
            total //= 10
            if total == 0:
                break

        stack.reverse() # digits should now be in the right order to be added to LL, TC O((n+m)%10) < O(n) <= O(m) < O(n+m)

        dummy = root = ListNode()
        while stack: # TC O((n+m)%10) < O(n) <= O(m) < O(n+m)
            digit = stack.pop()
            root.next = ListNode(digit)
            root = root.next
        
        return dummy.next

  '''
  TLDR: Iter through both LL, get sum, then use % and // with stack to get individual digits. Then, use the stack to create a new LL.

  TC O(n+m)
  SC O(n+m)
  '''
