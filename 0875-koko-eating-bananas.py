# NEETCODE Best Solution:
# The question is to find how many bananas should Koko eat in 1 hr to finish all bananas in h hours
# So let's take example- [3, 6, 7, 11]- there are 4 piles, each having respective number of bananas. 
# Here max no. of bananas in a piles is 11, so if Koko eats 11 bananas/hr, she'll finish all bananas in 4 hours
# (even if Koko eats > 11 bananas/hr, it'll take her 4 hours to finish all bananas, so there's no point of eating > 11 bananas)
# But she likes to eat slowly, so we need to find a min number to finish all the bananas.
# she can eat min 1 banana/hr and max max(piles) bananas/hr, so we'll do a Binary search in this range.
# calclate m and calculcate total hours taken to finish all bananas at that rate
# if total hours > h, it means the pace is too slow, and we need to search right
# if total hours <= h, that m could be a candidate for our answer so store that candidate(m) or calculate min of current m and previous res
# in the end, we'll do a minimum, and return res

# Time Complexity: O(log(max(p)) . P) where P is len(piles) and max(p) is the maximum element of piles array
# Space Complexity: O(1)

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            sumHrs = 0

            for i in piles:
                sumHrs += math.ceil(i / m)

            if sumHrs > h:
                l = m + 1
            else:
                r = m - 1
                res = min(res, m)
        
        return res   

--------------------------------------------------------------------------------------------------------------------------------------------------------
