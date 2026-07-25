import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []

        if k == 1:
            return nums

        for i in range(k - 1):
            heapq.heappush(heap, (-nums[i], i))
        
        p = k - 1
        l = len(nums)

        max_window = []

        while p < l:
            heapq.heappush(heap,(-nums[p],p))
            # print(heap)
            # print(p - k)
            # print()
            while heap[0][1] < p - k + 1:
                heapq.heappop(heap)
            max_window.append(-heap[0][0])
            p += 1
        
        return max_window
            
            