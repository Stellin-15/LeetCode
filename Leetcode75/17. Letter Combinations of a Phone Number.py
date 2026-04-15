class Solution(object):
    def letterCombinations(self, digits):

        if not digits: 
            return []
        
        mapping = {'2':"abc",'3':"def",'4':"ghi",'5':"jkl",'6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        results = []

        def backtrack(i, current):
            if i == len(digits):
                results.append(current)
                return 
        
            for letters in mapping[digits[i]]:
                backtrack(i+1, current + letters)

        backtrack(0,"")
        return results
    
    