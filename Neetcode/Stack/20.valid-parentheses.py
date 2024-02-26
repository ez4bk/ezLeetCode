#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:

    def isValid(self, s: str) -> bool:
        """
        Push to the stack if left parentheses, pop and check if match
        for right parentheses.
        """
        partner = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        topIndex = -1
        stack = []
        
        for c in s:
            if c in partner.keys():
                stack.append(c)
                topIndex += 1
            else:
                if stack and partner[stack[topIndex]] == c:
                    stack.pop(topIndex)
                    topIndex -= 1
                else:
                    return False
        
        if stack:
            return False
        
        return True

# @lc code=end
