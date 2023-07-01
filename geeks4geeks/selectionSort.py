#User function Template for python3

#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        _min = min(arr[i:])
        minIdx = i
        for j in range(i, len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
        return minIdx
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            minIdx = self.select(arr, i)
            arr[i], arr[minIdx] = arr[minIdx], arr[i]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends