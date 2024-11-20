#
# @lc app=leetcode id=20 lang=python3
# @lcpr version=20002
#
# [20] Valid Parentheses
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        stack = []
        for c in s:
            if c in dic:
                if not stack or stack.pop() != dic[c]:
                    return False
            else:
                stack.append(c)
        return not stack
# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

# @lcpr case=start
# "([])"\n
# @lcpr case=end

#

