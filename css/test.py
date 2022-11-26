# # def onlyPrimes(L):
# #     if L == []:
# #         return L
# #     else:
# #         if isPrime(L[0]-1, L[0]) and L[0] >= 2:
# #             return [L[0]] + onlyPrimes(L[1:])
# #         else:
# #             return onlyPrimes(L[1:])

# # def isPrime(factor, n):
# #     if factor <= 1:
# #         return True
# #     else:
# #         if n % factor == 0:
# #             return False
# #         return isPrime(factor-1, n)
    
# # def testisPrime():
# #     print("Testing isPrime...", end="")
# #     assert(isPrime(8, 9) == False)
# #     assert(isPrime(4, 5) == True)
# #     assert(isPrime(3, 4) == False)
# #     assert(isPrime(7, 8) == False)
# #     assert(isPrime(20, 21) == False)
# #     assert(isPrime(30, 31) == True)
# #     print("passed")

# # def testOnlyPrimes():
# #     print("Testing onlyPrimes...", end="")
# #     assert(onlyPrimes([]) == [])
# #     print(onlyPrimes([1,5,1,1,2]))
# #     assert(onlyPrimes([1, 5, 1, 1, 2]) == [5, 2])
# #     assert(onlyPrimes([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 5, 7])
# #     assert(onlyPrimes([6, -10, 3, 31, 21, -4, 12, 78, 10])
# #     == [3, 31])
# #     print("Passed!")
    
# # testisPrime()
# # testOnlyPrimes()

# # def replaceIntSquareSum(L):
# #     L = flatten(L)
# #     # print(L)
# #     return sum(L)

# # def flatten(L):
# #     if L == []:
# #         return L
# #     else:
# #         if isinstance(L[0], list):
# #             return flatten(L[0]) + flatten(L[1:])
# #         else:
# #             return [L[0]] + flatten(L[1:])
    
# # def sum(L):
# #     if L == []:
# #         return []
# #     else:
# #         if isinstance(L[0], int):
# #             # print(f"found int: {L[0]}")
# #             number = 0
# #             while L[0] > 0:
# #                 last_digit = L[0] % 10
# #                 number += last_digit * last_digit
# #                 L[0] //= 10
# #             # print(f"number: {number}")
# #             # print(L[1:], sum(L[1:]))
# #             return [number] + sum(L[1:])
# #         else:
# #             return sum(L[1:])
            
# # def testReplaceIntSquareSum():
# #     print("Testing replaceIntSquareSum...")
# #     L = [24, 'hi', ['hello', 42, 'there', [112, 'kenobi'], 15], 11]
# #     assert(replaceIntSquareSum(L) == [20, 20, 6, 26, 2])
# #     L = [12, 35, 'bleh', ['test1!', 5555, [666, set(), dict()], dict()], 13]
# #     assert(replaceIntSquareSum(L) == [5, 34, 100, 108, 10])
# #     L = ['hello', 'there']
# #     assert(replaceIntSquareSum(L) == [])
# #     print("Passed!")
    
# # testReplaceIntSquareSum()

# # s = "1234"

# # print(s[:2])

# # def ct1(s):
# #     if len(s) <= 1:
# #         return s
# #     else:
# #         i = len(s)//2
# #         return s[i] + ct1(s[i+1:]) + ct1(s[:i])
    
# # print(ct1('35126'))

# # def ct2(n):
# #     if n < 10:
# #         return [n]
# #     else:
# #         return [n%10] + ct2(n//100)
# # print(ct2(12345))
    
# # def biggest(L):
# #     if L == []:
# #         return 0
# #     else:
# #         if L[0] > biggest(L[1:]):
# #             return L[0]
# #         else:
# #             return biggest(L[1:])

# # def second(L, biggest, count):
# #     if L == []:
# #         return 0
# #     else:
# #         if L[0] == biggest:
# #             count += 1
# #         if L[0] >= second(L[1:], biggest, count) and count >= 2:
# #             return L[0]
# #         elif L[0] >= second(L[1:], biggest, count) and L[0] != biggest:
# #             return(L[0])
# #         else:
# #             return second(L[1:], biggest, count)
        

# # def secondLargest(L):
# #     if L == []:
# #         return None
# #     elif len(L) == 1:
# #         return None
# #     else:
# #         big = biggest(L)
# #         return second(L, big, 0)

# # def vowelRun(s):
# #     if len(s) == 0:
# #         return 0
# #     else:
# #         if s[0].lower() in {'a', 'e', 'i', 'o', 'u'}:
# #             return 1 + vowelRun(s[1:])
# #         else:
# #             return 0

# # def longestVowelRun(s):
# #     if len(s) == 0:
# #         return 0
# #     else:
# #         x = vowelRun(s)
# #         if x > longestVowelRun(s[1:]):
# #             return x
# #         else:
# #             return longestVowelRun(s[1:])

# def largest(L):
#     if L==[]:
#         return 0
#     else:
#         if L[0] > largest(L[1:]):
#             return L[0]
#         else:
#             return largest(L[1:])
        
# def second(L, count):
#     if L==[]:
#         return 0
#     else:
#         max = largest(L)
#         if count == 2:
#             return L[0]
#         if L[0] == max:
#             return second(L[1:], count+1)
#         elif L[0] > second(L[1:], count) and L[0]<max:
#             return L[0]
#         else:
#             return second(L[1:], count)
        
# def secondLargest(L):
#     if L == [] or len(L) == 1:
#         return None
#     else:
#         return second(L, 0)
    

# def testSecondLargest():
#     print("Testing second largest")
#     print((secondLargest([2,5,3,4,1])))
#     assert(secondLargest([2,5,3,4,1]) == 4)
#     assert(secondLargest([6,5,6,6,6]) == 6)
#     assert(secondLargest([1]) == None)
#     assert(secondLargest([]) == None)
#     print("Passed")
    
# testSecondLargest()

# def testVowelRun():
#     print("Testing vowel run")
#     assert(vowelRun('abaeiou') == 1)
#     assert(vowelRun('daeiou') == 0)
#     assert(vowelRun('aeiobu') == 4)
#     print("passed")

# def testLongestVowelRun():
#     print("Test longest vowel run")
#     assert(longestVowelRun('AbcAeiD aEoa ba') == 4) # aEoa
#     assert(longestVowelRun('cnsnts') == 0) # no vowels
#     assert(longestVowelRun('aeiouAEIOU') == 10) # all vowels
#     print("Passed")
    
# testVowelRun()
# testLongestVowelRun()