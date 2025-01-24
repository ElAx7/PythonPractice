#Design an algorithm to encode a list of strings to a single string. 
#The encoded string is then decoded back to the original list of strings.

#Please implement encode and decode

from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}:{s}" for s in strs) #Devuelve una cadena con la longitud de cada cadena y la cadena

    def decode(self, s: str) -> List[str]:
        strs = [] #Lista de cadenas vacía 
        i = 0 #Variable de inicio en 0 
        while i < len(s): #Mientras la variable de inicio sea menor a la longitud de la cadena 
            j = s.find(':', i) #Encuentra el índice de la cadena desde la variable de inicio hasta el final de la cadena 
            i = j + 1 + int(s[i:j]) #La variable de inicio es igual al índice de la cadena más 1 más la longitud de la cadena
            strs.append(s[j+1:i]) #Añade a la lista de cadenas la cadena desde el índice de la cadena más 1 hasta la variable de inicio
        return strs #Devuelve la lista de cadenas 
    
print(Solution().encode(["hola", "mundo"])) # "4:hola5:mundo"
