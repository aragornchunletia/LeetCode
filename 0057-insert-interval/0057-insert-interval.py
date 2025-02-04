class Solution:
    """
    Binary Search
    the intervals that end before newInterval go to the left,
    the intervals that start after newInterval ends go to the right
    the contested intervals are merged to form newInterval
    """
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        joint = newInterval
        left , right = [] , []
        for interval in intervals:
            if interval[1] < newInterval[0]:
                left.append(interval)
            elif  interval[0] > newInterval[1]:
                right.append(interval)
            else:
                joint[0] = min(joint[0] , interval[0])
                joint[1] = max(joint[1] , interval[1])

        return left + [joint] + right

