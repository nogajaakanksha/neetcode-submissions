class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        res = float("inf")

        # piles = [3,6,7,11], h = 8
        # 3, 4, 5, 6, 7, 8, 9, 10, 11
        # 7 -> 5

        while l <= r:
            mid = (l + r) // 2
            # count the houts for mid speed
            hours = 0
            for p in piles:
                hours += math.ceil(p / mid)           
            if hours <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res