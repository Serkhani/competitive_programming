class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        _max = -1
        for i in range(len(arr)-1,-1,-1):
            arr[i], _max = _max, max(_max, arr[i])
            
        # while i>0:
        #     _max = max(arr[i+1:])
        #     maxIndex = arr.index(_max)
        #     arr[i:maxIndex] = [_max for i in range(maxIndex-i)]
        #     i += (maxIndex-i)
        # arr[len(arr)-1] = -1
        return arr