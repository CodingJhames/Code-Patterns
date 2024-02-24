
# Build Array from Permutation

def buildArray(nums):
  n = len(nums)
  for i in range(0, len(nums)):
      nums[i]=nums[i]+(n*(nums[nums[i]]%n))

  for i in range(0, len(nums)):
      nums[i] = int(nums[i]/n)

  return nums

nums = [0,2,1,5,3,4]

# print(buildArray(nums))

# Escriba una función que le sirva para reconocer si una palabra es o no palíndrome (se lee igual al derecho y al revés). Su función sólo debe utilizar slices.

def palindrome( word ):
  if word[::-1] == word[0:]:
    return True
  else:
    return False
    
# print(palindrome(""))

# word = 'anilina'
# print(word[::-1])
# print(word[0:])


def recur_factorial(n):
  fact=1
  for i in range(2,n+1):
    fact*=i
  return fact  
# print(recur_factorial(5))

# def recur_factorial(n):
#   if n==1:
#     return n
#   else:
#     temp=recur_factorial(n-1)
#     return temp*n
    
# print(recur_factorial(5))

def permute(string, pocket=""):
  if len(string)==0:
    print(pocket)
  else:
    for i in range(len(string)):
      letter = string[i]
      front = string[0:i]
      back = string[i+1:]
      together = front + back
      permute(together, letter + pocket)

# print(permute("ABC"))

def reverseString( s ):
  inverted=s[::-1]
  print(inverted)

# reverseString(s = ["h","e","l","l","o"])

# def print_rangoli(size):
#   alpha=[chr(i) for i in range(97, 123)]
#   alpha=alpha[:size]

#   indices=list(range(size))
#   indices=indices[:1]+indices[::-1]

#   for i in indices:
#     start_index=i+1
#     original=alpha[-start_index:]
#     reverse=original[::-1]
#     row=reverse+original[1:]
#     row="-".join(row)
#     width=size*4-3
#     row=row.center(width, "-")
#     print(row)

# def solve(s):
#   s=s.split()
#   for i in range(len(s)):
#     s[i]=s[i].capitalize()
    
#   s=" ".join(s)
#   return s

# def solve(s):
#   s=s.split()
#   for i in range(len(s)):
#       s[i]=s[i].capitalise()

#   s=" ".join(s)
#   print(s)

# print(solve("jhames mejia"))

# def groupAnagrams( strs):
#   anagrams = {}
#   for word in strs:
#     sorted_word = ''.join(sorted(word))
#     if sorted_word not in anagrams:
#       anagrams[sorted_word] = []
#     anagrams[sorted_word].append(word)
#   return list(anagrams.values())

# strs = ["eat","tea","tan","ate","nat","bat"]

# print(groupAnagrams(strs))

# from itertools import product

# A = list( map(int, input().split(' ')) )
# B = list( map(int, input().split(' ')) )

# for i in product( A,B):
#   print(i, end=" ")

# 08/02/2024

# class Solution:
#   def getDecimalValue(self, head: ListNode) -> int:
#       for i in head:
#           cadenas = list(map(str, head))
#           result = ''.join(cadenas)
#           decimal = int(result, 2)
#       print("Entero:", decimal)


# head = [1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,1,0,1,1,0,]
# getDecimalValue( head )

# def sortedSquares(nums):
#   start, end = 0, len(nums)-1
#   arr = []

#   while nums[start] < nums[end]:
#     arr.append(nums[start]**2)
#     arr.append(nums[end]**2)
#     start += 1
#     end -=1
#     arr.sort()
#     print(arr)
#   return arr

# sortedSquares([-4,-1,0,3,10])


# n = len(nums)
# l = 0
# r = n - 1
# ans = [0] * n

# while n:
# n -= 1
# if abs(nums[l]) > abs(nums[r]):
#     ans[n] = nums[l] * nums[l]
#     l += 1
# else:
#     ans[n] = nums[r] * nums[r]
#     r -= 1

# return ans

