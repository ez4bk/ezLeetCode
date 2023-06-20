#
# @lc app=leetcode id=551 lang=python3
#
# [551] Student Attendance Record I
#

# @lc code=start
class Solution:
    def checkRecord(self, s: str) -> bool:
        attendance = {'A': 0, 'L': 0}
        for char in s:
            if char == 'A':
                attendance['A'] += 1
                attendance['L'] = 0
                if attendance['A'] > 1:
                    return False
            elif char == 'L':
                attendance['L'] += 1
                if attendance['L'] > 2:
                    return False
            else:
                attendance['L'] = 0
        return True

# @lc code=end
