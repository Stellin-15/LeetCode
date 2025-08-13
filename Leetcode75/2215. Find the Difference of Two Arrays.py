class Solution(object):
    def findDifference(self, nums1, nums2):

        set1 , set2 = set(nums1) , set(nums2) # remove duplicates
        only_in_1 = list(set1 - set2 ) # elements in set1 but not in set2
        only_in_2 = list(set2 - set1 )  # elements in set2 but not in set1

        return [only_in_1 ,only_in_2]