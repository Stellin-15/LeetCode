class Solution(object):
    def mergeAlternately(self, word1, word2):
            newWord = ""
            i = 0
            j = 0

            while i < len(word1) and j < len(word2):
                newWord += word1[i] + word2[j] 
                i += 1
                j += 1


            newWord += word1[i:] + word2[j:] 

            return newWord