#Given an integer array nums, return an array output where output[i] is 
#the product of all the elements of nums except nums[i].

#Each product is guaranteed to fit in a 32-bit integer.

#Follow-up: Could you solve it in O(n) time complexity without using division?


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums) #Longitud de la lista de números
        ouput = [1] * n #Lista de unos de longitud n
        left = 1
        right = 1
        for i in range(n):
            ouput[i] *= left
            ouput[n - 1 - i] *= right
            left *= nums[i]
            right *= nums[n - 1 - i]
        return ouput
    
print(Solution().productExceptSelf([1, 2, 3, 4])) # [24, 12, 8, 6]
        