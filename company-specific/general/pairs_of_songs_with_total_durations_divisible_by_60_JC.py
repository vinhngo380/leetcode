class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Utilize remainders! If we have remainders, we can add 60 - remainder to the pairs res.
        # ex: if we have numbers of 100 and 20, then the remainder will be 20 and 40 respectively.
        # Such that [20]: 100, [40]: 20. These two 100 + 20 will make a pair, as 100 + 20 == 120 % 60 = 0

        remainders = defaultdict(int)
        pairs = 0
        for i in range(len(time)):
            if time[i] % 60 == 0:
                pairs += remainders[0] # remainders[0] NOT 1. This is due to pairs, and if we had ex: [7,7,7] we won't have 3 pairs, but 2 pairs.
            else:
                pairs += remainders[60 - (time[i] % 60)] # the expression 60 - (time[i] % 60) is derived from 60 - (remainder), like 150 % 60 == 30
            remainders[time[i] % 60] += 1
        return pairs

'''
TLDR: Utilize remainders, while considering a two-sum-like implementation. Note what we are ADDING, which is pulling from remainders[time[i]]. 
This is due to considering the pairs. Also consider 60 - (time[i] % 60)... remainder is 60 - (time % 60).

TC: O(n)
SC: O(59) => O(1)
'''


