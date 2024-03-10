# Given an unsorted array arr[] of n integers and a key which is present in this array. You need to write a program to find the start index( index where the element is first found from left in the array ) and end index( index where the element is first found from right in the array ).(0 based indexing is used)
# If the key does not exist in the array then return -1 for both start and end index in this case.
# Example 1:
# Input:
# arr[] = { 1, 2, 3, 4, 5, 5 }
# key = 5
# Output:  {4, 5}

class Solution():
    arr = [1,2,3,4,5,5]
    def findIndex(self,key):
        index1 = self.arr.index(key) # to find the index of the key element
        x = index1+1
        y = index1-1
        print(self.arr[y:x])

obj = Solution()
obj.findIndex(3)




