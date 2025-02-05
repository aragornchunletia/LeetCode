from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        Determines the starting gas station index from which the car can travel around 
        the circuit once in a clockwise direction without running out of gas.

        Returns:
        int: The starting gas station index if a complete circuit is possible; otherwise, -1.

        Approach:
        - First, check if the total gas available is less than the total cost required. 
          If so, return -1, since a complete trip is impossible.
        - Compute the difference `diff[i] = gas[i] - cost[i]` at each station.
        - Use a greedy approach: 
          - Keep track of the running sum (`total`).
          - If `total` becomes negative at any station `i`, reset `total` and assume the 
            next station `i+1` as the new starting point.
        - The algorithm works because if a valid start exists, it must be in the last segment 
          where the total sum remains non-negative.
        """

        # If the total available gas is less than the total cost, no solution exists.
        if sum(gas) < sum(cost):
            return -1
        
        # Compute the net fuel at each station.
        diff = [a - b for a, b in zip(gas, cost)]
        
        total = 0
        start = 0  

        # Iterate through the stations to find a valid start
        for i, val in enumerate(diff):
            total += val  
            
            # If at any point the total balance goes negative, reset
            if total < 0:
                total = 0    # Reset total balance
                start = i + 1  # Set next station as the new potential start
        
        return start  
