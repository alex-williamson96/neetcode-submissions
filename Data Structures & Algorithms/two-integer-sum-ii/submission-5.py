class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(numbers) - 1
        while p1 < p2:
            val = numbers[p1] + numbers[p2]
            if val == target:
                return [p1 + 1, p2 + 1]
            
            if val > target:
                p2 -= 1
            else:
                p1 += 1