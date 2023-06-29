class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        idx = arr.index(max(arr))
        if not idx or idx == len(arr)-1:
            return False
        for i in range(idx,0,-1):
            if arr[i]<arr[i-1] or arr[i-1] == arr[i]:
                return False

        for i in range(idx,len(arr)-1):
            if arr[i+1]>arr[i] or arr[i+1] == arr[i]:
                return False
        return True
    
# Time Complexity
# O(n)
# Space Complexity
# O(1)

