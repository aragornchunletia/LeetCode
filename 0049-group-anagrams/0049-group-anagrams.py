class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        count_dict = {}
        for s in strs:
            #char hash update char counts
            counter = [0]*26
            for c in s:
                counter[ord(c)-ord('a')] += 1
            #lists are not hashable so convert to a tuple
            #add to a dict and voila
            counter = tuple(counter)
            if counter not in count_dict:
                count_dict[counter] = [s]
            else:
                count_dict[counter].append(s)

        return list(count_dict.values())
            
                