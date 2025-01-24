#Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Boolean) según sean o no anagramas.
# Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# NO hace falta comprobar que ambas palabras existan.
# Dos palabras exactamente iguales no son anagrama.

def anagram(word_one, word_two): 
    if word_one.lower() == word_two.lower(): 
        return False 
    return sorted(word_one.lower()) == sorted(word_two.lower()) 

print(anagram("roma", "amor")) # True

#Otra forma de hacerlo

def anagrama(word1, word2):
    return sorted(word1) == sorted(word2)

def main():
    print(anagrama("roma", "amor")) # True
    print(anagrama("hola", "hello")) # False

if __name__ == "__main__":
    main()

#Ejercicio de LeetCode
   
#Given two strings s and t, return true if the two strings are anagrams of each other, 
#otherwise return false.
#An anagram is a string that contains the exact same characters as another string,
#but the order of the characters can be different.

from typing import str

class Solution:
    def isAnagram(self, s: str, t: str) -> bool: 
        return sorted(s) == sorted(t)
    
