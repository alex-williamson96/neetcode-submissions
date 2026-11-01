class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums2, nums1 = nums1, nums2
        
        l = 0
        r = len(nums1)
        half = (len(nums1) + len(nums2)) // 2

        while l <= r:
            cut1 = (l + r) // 2
            cut2 = half - cut1

            l1 = nums1[cut1 - 1] if cut1 > 0 else float('-inf')
            r1 = nums1[cut1] if cut1 < len(nums1) else float('inf')
            l2 = nums2[cut2 - 1] if cut2 > 0 else float('-inf')
            r2 = nums2[cut2] if cut2 < len(nums2) else float('inf')

            if l1 > r2:
                r = cut1 - 1
            elif l2 > r1:
                l = cut1 + 1
            else:
                if (len(nums1) + len(nums2)) % 2 == 0:
                    return (max(l1,l2) + min(r1,r2)) / 2
                else:
                    return min(r1,r2)



        
