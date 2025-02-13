from bisect import bisect_left
from typing import List

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()  # Step 1: Sort lexicographically
        res = []
        prefix = ""

        for char in searchWord:
            prefix += char  # Build the prefix step by step
            index = bisect_left(products, prefix)  # Step 2: Binary search for prefix
            
            # Step 3: Collect up to 3 lexicographically smallest matching products
            suggestions = []
            for i in range(index, min(index + 3, len(products))):
                if products[i].startswith(prefix):
                    suggestions.append(products[i])
                else:
                    break
            
            res.append(suggestions)
        
        return res
