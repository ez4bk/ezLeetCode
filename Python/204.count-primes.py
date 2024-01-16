#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False
        for i in range(2, n):
            if isPrime[i]:
                j = 2
                while i*j < n:
                    isPrime[i*j] = False
                    j += 1
        return sum(isPrime)
        # if n < 3:
        #     return 0
        # primes = [True] * n
        # primes[0] = primes[1] = False
        # for i in range(2, int(n ** 0.5) + 1):
        #     if primes[i]:
        #         primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        # return sum(primes)
    # @lc code=end
