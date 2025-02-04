class Solution:
    """
    This problem was my nemesis took too long
    the trick was keep track of the number changes we need to make 
    """
    def minWindow(self, s: str, t: str) -> str:

        tCounter = {}
        #lenOfMinString , startIndx , endIndx
        minString = (float('inf') , 0 ,0)
        #char count of t string
        for char in t:
            tCounter[char]  = tCounter.get(char , 0) + 1
        #char count of s string
        sCounter = {key : 0 for key in tCounter.keys()}
        start , end = 0 , 0
        change = len(sCounter)

        while end < len(s):

            char = s[end]
            if char in sCounter:
                sCounter[char] += 1
                if sCounter[char] == tCounter[char]:
                    change -= 1
            #change = Zero, we have found the substr
            #move start pointer untill the change is no more 0
            while change == 0:
                if end - start < minString[0]:
                    minString = (end-start,start , end+1)
                
                sChar = s[start]
                if sChar in sCounter:
                    sCounter[sChar] -= 1
                    if sCounter[sChar] < tCounter[sChar]:
                        change += 1

                start += 1

            end += 1

        return s[minString[1] : minString[2]] if minString[0] != float('inf') else ""




                        


        





        