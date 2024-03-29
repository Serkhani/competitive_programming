class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ptr1, ptr2 = 0,0
        nums1.sort()
        nums2.sort()
        output = set()
        while ptr1<len(nums1) and ptr2<len(nums2):
            if nums1[ptr1]<nums2[ptr2]:
                ptr1+=1
            elif nums2[ptr2]<nums1[ptr1]:
                ptr2+=1
            else: 
                output.add(nums1[ptr1])
                ptr1 += 1
                ptr2 += 1
        return list(output)