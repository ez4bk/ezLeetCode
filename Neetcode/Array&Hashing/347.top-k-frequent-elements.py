#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        We record the frequency for each element in a dict.
        We then extract the key with the highest value/frequency out
        and make it 0 to remove it from the record.
        """
        counter = {}
        for n in nums:
            if not counter.get(n):
                counter[n] = 0
            counter[n] += 1
            
        res = []
        while k > 0:
            max_key = max(counter, key=counter.get)
            res.append(max_key)
            counter[max_key] = 0
            k -= 1
        return res
        
# @lc code=end

