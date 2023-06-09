class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]: 
        largest = arr[len(arr)-1]
        for i in range(len(arr)-2, -1, -1):
            if arr[i] > largest:
                largest = arr[i]
                arr[i] = arr[i+1]
            arr[i] = largest
        arr.pop(0)
        arr.append(-1)
        return arr           