# Given an array arr of size n, print all its elements space-separated.
#
# Note: You don't need to move to the next line after printing all elements of the array (space-separated)
#
# Example 1:
#
# Input:
# n = 5
# arr[] = {1, 2, 3, 4, 5}
# Output: 1 2 3 4 5


class Solution:

	def printArray(self,arr):

	    for num in arr:
	        print(num,end=' ') # end = '' will print nums horizontally1
arr = Solution()
arr.printArray(input())
