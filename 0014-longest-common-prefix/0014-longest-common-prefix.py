class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()
        small = strs[0]
        large = strs[-1]
        result = ""

        for i in range(len(small)):

            if small[i] != large[i]:
                break
            else:
                result += small[i]

        return result 
