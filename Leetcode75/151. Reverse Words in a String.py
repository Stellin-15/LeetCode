class Solution(object):
    def reverseWords(self, s):
        temp = s.split()
        temp.reverse()
        return " ".join(temp)
