#
# @lc app=leetcode id=520 lang=python3
#
# [520] Detect Capital
#


# @lc code=start
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # if word[0] == word[0].upper():
        #     if len(word) == 1:
        #         return True
        #     if word[1] == word[1].upper():
        #         for i in range(2, len(word)):
        #             if word[i] != word[i].upper():
        #                 return False
        #     else:
        #         for i in range(2, len(word)):
        #             if word[i] != word[i].lower():
        #                 return False
        # else:
        #     for i in range(1, len(word)):
        #         if word[i] != word[i].lower():
        #             return False
        # return True

        return word.match(r"[A-Z]*|.[a-z]*")


# @lc code=end
