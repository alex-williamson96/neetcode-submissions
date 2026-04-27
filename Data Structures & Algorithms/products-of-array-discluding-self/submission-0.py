class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        total = 1
        zero_index = 0

        for i, num in enumerate(nums):
            if num == 0:
                zero_count += 1
                zero_index = i
                continue
            if zero_count > 1:
                break
            total *= num
        
        if zero_count > 1:
            return [0 for num in nums]
        
        if zero_count == 1:
            r = [0 for num in nums]
            r[zero_index] = total
            return r
        
        return [int(total/num) for num in nums ]
