class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        p = k -1

        l = len(nums)

        m = []
        w = []

        for i in range(k - 1):
            w.append(nums[i])

        while p <= l - 1:
            w.append(nums[p])
            m.append(max(w))
            p += 1
            del w[0]

        
        return m