#Given an integer array nums, return true if any value
#appears more than once in the array, otherwise return false.

from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}  # Diccionario para contar las frecuencias de los números
        for n in nums: # Iterar sobre los números
            count[n] = 1 + count.get(n, 0) # Contar las frecuencias de cada número
            if count[n] > 1: # Si la frecuencia de un número es mayor a 1
                return True # Retornar True
        return False # Si no hay números repetidos, retornar False
    
# Ejemplo de uso:
solution = Solution()
print(solution.hasDuplicate([1,2,3,1]))  # Salida: True
print(solution.hasDuplicate([1,2,3,4]))  # Salida: False