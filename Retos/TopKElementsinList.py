#Given an integer array nums and an integer k, return the k most frequent elements within the array.
#The test cases are generated such that the answer is always unique.
#You may return the output in any order.

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for _ in range(len(nums) + 1)]

        # Contar las frecuencias de cada número
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # Agrupar números por sus frecuencias
        for n, c in count.items():
            freq[c].append(n)

        res = []
        # Iterar sobre las frecuencias desde la más alta hasta la más baja
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# Ejemplo de uso:
solution = Solution()
print(solution.topKFrequent([1,1,1,2,2,3], 2))  # Salida: [1, 2]

