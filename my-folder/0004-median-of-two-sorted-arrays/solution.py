import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        li=[]
        li=nums1+nums2
        li.sort()
        
        if(len(li)%2 == 0):
            ind1 = len(li)//2
            #print(ind1)
            return (li[ind1]+li[ind1-1])/2
            
        else:
            ind = len(li)//2
            return li[ind]
        
        
        
        
        
