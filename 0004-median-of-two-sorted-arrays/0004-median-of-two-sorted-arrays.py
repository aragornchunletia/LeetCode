class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        if len(nums1) > len(nums2):
            nums1 , nums2 = nums2 , nums1 #ensuring nums1 is always the smaller one

        l , r = 0 , len(nums1)
        odd = (len(nums1) + len(nums2)) % 2 == 1

        while l <= r:
            pointerA  = (l+r) // 2
            pointerB = (len(nums1) + len(nums2) + 1) // 2 - pointerA

            maxLA = float('-inf') if pointerA == 0 else nums1[pointerA - 1]
            minRA = float('inf') if pointerA == len(nums1) else nums1[pointerA]
            maxLB = float('-inf') if pointerB == 0 else nums2[pointerB - 1]
            minRB = float('inf') if pointerB == len(nums2) else nums2[pointerB]

            if maxLA <= minRB and maxLB <= minRA:
                return max(maxLA , maxLB) if odd else (max(maxLA , maxLB) + min(minRA , minRB))/2
            elif maxLA > minRB:
                r = pointerA - 1
            elif minRA > maxLA:
                l = pointerA + 1

        
        