#
# @lc app=leetcode id=500 lang=python3
#
# [500] Keyboard Row
#


# @lc code=start
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        keyboard_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        keyboard_map = {}

        for row in keyboard_rows:
            for c in row:
                keyboard_map[c] = keyboard_rows.index(row)
        for i in range(len(words)):
            row = keyboard_map[words[i][0].lower()]
            for c in words[i]:
                if keyboard_map[c.lower()] != row:
                    words[i] = ""
                    break
        return " ".join(words).split()


# @lc code=end
