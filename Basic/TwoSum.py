#Two Sums
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.

class Solution:
    def twoSum(self, nums, target):
        hash = {} #tabla has para guardar los indices de los numeros
        for i in range(len(nums)): #recorrer el arreglo de numeros 
            if target - nums[i] in hash: #si el numero que se necesita para completar el target esta en la tabla hash
                return [hash[target - nums[i]], i] #regresar los indices de los numeros que suman el target
            hash[nums[i]] = i #si no se encuentra el numero que se necesita para completar el target, se guarda el numero en la tabla hash
        return [] #si no se encuentra ningun par de numeros que sumen el target, regresar un arreglo vacio