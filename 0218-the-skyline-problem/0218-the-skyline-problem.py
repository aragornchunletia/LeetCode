from sortedcontainers import SortedList
class Solution:
    """
    Line Sweep problem
    """
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:

        events = collections.defaultdict(list)
        # -1 start of a building, 1 end of a building
        for left,right,h in buildings:
            events[left].append((-1,h))
            events[right].append((1,h))

        sl = SortedList()
        #starting height = 0
        sl.add(0)
        
        res = []
        lastH = 0
        for x in sorted(events.keys()):
            for t,h in events[x]:
                #new building started
                if t==-1:
                    sl.add(h)
                #A building just ended
                else:
                    sl.remove(h)
            #the heighest height currently
            currentH = sl[-1]
            #there has been a change in the silhouette
            if currentH != lastH:
                res.append((x,currentH))
            lastH = currentH

        return res








