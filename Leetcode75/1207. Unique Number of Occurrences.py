class Solution(object):
    def uniqueOccurrences(self, arr):

        collection = { }

        for num in arr:
            collection[num] = collection.get(num, 0) + 1

        return len(collection.values()) == len(set(collection.values())) 