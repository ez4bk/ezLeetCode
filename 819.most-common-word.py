#
# @lc app=leetcode id=819 lang=python3
#
# [819] Most Common Word
#


# @lc code=start
from collections import defaultdict
import operator


class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        banned = set(banned)
        paragraph = paragraph.lower()
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        words = paragraph.split()
        words = [w for w in words if w not in banned and w != ""]

        word_count = defaultdict(int)

        for w in words:
            if w not in banned:
                word_count[w] += 1

        return max(word_count.items(), key=operator.itemgetter(1))[0]


# @lc code=end
