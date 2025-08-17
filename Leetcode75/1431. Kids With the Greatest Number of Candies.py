class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies = max(candies)
        results = []

        for i in range(len(candies)):
            results.append(candies[i] + extraCandies >= maxCandies)
        return results