"""
Do we count duplicates?
E.g. 1,2,2,3 | 3, Ans 1 or 2?
What values can k take?
What if n < k?
Can transform k to min(k,n-k+1)?
Input: list of numbers? Sorted?
What kind of numbers? Ints?
Do numbers have a min or max?

Normal sort (n log n)
Min heap of size k (n log k) (heapq)
Quickselect (avg n, worst n^2)
Bucket sort of frequencies (n+m,
m = high - low + 1)

MWE: 1,2,3,4,5 | 2 -> 4

Ans: quickselect(nums, k) or bucket
quickselect(list, val)
random.choice(list) for pivot
left/right/mid = nums <>= pivot
if right >= k: 
return quickselect(right, k)
elif right + mid < k: 
return quickselect(left, k-right-mid)
else return pivot
Master theorem: T(n) = T(n/2) + O(n)
TC: O(N) avg, O(N^2) worst   SC: O(N)
"""

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        def quickselect(clist, creq):
            pivot = random.choice(clist)
            left = []
            mid = []
            right = []
            for n in clist:
                if n < pivot:
                    left.append(n)
                elif n > pivot:
                    right.append(n)
                else:
                    mid.append(n)

            if len(right) >= creq:
                return quickselect(right, creq)
            elif len(right) + len(mid) < creq:
                return quickselect(left, creq-len(right)-len(mid))
            return pivot

        return quickselect(nums, k)