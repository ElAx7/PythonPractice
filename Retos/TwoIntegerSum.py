#Given an array of integers nums and an integer target, return the indices i and j such that 
#nums[i] + nums[j] == target and i != j.
#You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
#Return the answer with the smaller index first.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)): #Recorre la lista de números
            for j in range(i+1, len(nums)): #Recorre la lista de números desde el siguiente número al actual
                if nums[i] + nums[j] == target: #Si la suma de los números es igual al objetivo
                    return [i, j] #Devuelve los índices de los números


print(Solution().twoSum([2,7,11,15], 9)) # [0, 1]

# len: O(n^2) - Quadratic time  - Recorre la lista de números dos veces 
