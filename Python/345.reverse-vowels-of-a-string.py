#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#


# @lc code=start
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [
            ord("a"),
            ord("e"),
            ord("i"),
            ord("o"),
            ord("u"),
            ord("A"),
            ord("E"),
            ord("I"),
            ord("O"),
            ord("U"),
        ]
        head = 0
        tail = len(s) - 1
        s = list(s)
        while head <= tail:
            if ord(s[head]) in vowels:
                while tail > head:
                    if ord(s[tail]) in vowels:
                        s[head], s[tail] = s[tail], s[head]
                        break
                    tail -= 1
                tail -= 1
            head += 1
        # while head < tail:
        #     if ord(s[head]) in vowels and ord(s[tail]) in vowels:
        #         s[head], s[tail] = s[tail], s[head]
        #         head += 1
        #         tail -= 1
        #     elif ord(s[head]) not in vowels:
        #         head += 1
        #     elif ord(s[tail]) not in vowels:
        #         tail -= 1
        return "".join(s)


# @lc code=tail
