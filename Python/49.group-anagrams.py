#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = []
        dict = {
            # "word_sorted": ["word1", "word2"]
        }
        for word in strs:
            word_sorted = ""
            for _ in sorted(word):
                word_sorted = word_sorted + _
            if dict.get(word_sorted):
                dict[word_sorted].append(word)
            else:
                dict[word_sorted] = [word]

        for value in dict.values():
            res.append(list(value))

        return res
# @lc code=end
