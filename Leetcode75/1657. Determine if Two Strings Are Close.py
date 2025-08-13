from collections import Counter

class Solution(object):
    def closeStrings(self, word1, word2):
        if len(word1) != len(word2): return False 

        count1 = Counter(word1)
        count2 = Counter(word2)

        if set(count1.keys()) != set(count2.keys()):   # 3. Same set of characters?
            return False

        if sorted(count1.values()) != sorted(count2.values()):  # 4. Same multiset of frequencies?
            return False
        


        return True 

        

        