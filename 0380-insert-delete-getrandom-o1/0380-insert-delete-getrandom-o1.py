import random

class RandomizedSet:
    """
    INSERT -> O(1)
    if element not in the set
    add element to the end of the list
    store its Idx in a Map

    REMOVE -> O(1)
    if element in Set
    get its index
    swap its posotion with the last element
    update the map
    -> lastEle:map[val]
    map.delete(val)
    array.pop()

    GET RANDOM: O(1)
    use random to generate a random number between 0,len(array)
    return the val
    """

    def __init__(self):
        self.array = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.array.append(val)
        self.map[val] = len(self.array) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        # Get the index of the value to remove and swap with last value
        idx = self.map[val]
        lastElement = self.array[-1]
        self.array[idx] , self.array[-1] = self.array[-1] , self.array[idx]
        if lastElement != val:
            self.map[lastElement] = idx
        

        # Remove the last element
        self.array.pop()
        del self.map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.array)
