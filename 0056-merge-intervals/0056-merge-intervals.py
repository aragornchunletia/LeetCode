from collections import deque
"""
Seems a greedy solution after sorting
1.start with the interval that starts the earliest
2.push it onto the stack
3.comapre next intervals with previous ones
    -> if previous ends before this interval starts join interval
    -> else append to the stack and move on
4.the resultant stack is the answer
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[0])

        stack = deque([])

        for interval in intervals:
            if not stack:
                stack.append(interval)
            elif stack[-1][1] >= interval[0]:
                temp = stack.pop()
                stack.append([temp[0], max(temp[1], interval[1])])
            else:
                stack.append(interval)

        return list(stack)







