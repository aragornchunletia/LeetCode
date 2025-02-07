from heapq import heappop , heappush
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num , 0) + 1

        minq = []

        for num , frq in freq.items():
            if len(minq) < k:
                heappush(minq , (frq , num))
            else:
                if minq[0][0] < frq:
                    heappop(minq)
                    heappush(minq , (frq,num))


        return [ele for f,ele in minq]
        