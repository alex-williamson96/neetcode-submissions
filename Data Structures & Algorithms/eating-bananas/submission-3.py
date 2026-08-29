class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        best_k = right

        while left <= right:
            k = (left + right) // 2

            time_taken = sum([(p + k - 1) // k for p in piles])
            if time_taken <= h:
                right = k - 1
                if k < best_k:
                    best_k = k
            else:
                left = k + 1
        
        return best_k
        