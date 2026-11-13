# #Exercise 1
# def is_odd(n):
#     if n % 2 == 0:
#         return False
#     else:
#         return True
# output = is_odd(5)
# print(output)
from unittest import result


# #Exercise 2
# def leap_year(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
# print(leap_year(2000))

# #Exercise 3
# def print_triangular_numbers(n):
#     x = 0
#     for i in range(0, n):
#         x = x + i+1
#         print(i+1, x)
#     return x
# print(print_triangular_numbers(5))
# print(print_triangular_numbers(10))

# #Exercise 4
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             print("Number can be divided by", i)
#             return False
#     return True
#
# print(is_prime(72))

# #Exercise 5
# def reverse_string(s):
#     result = ""
#     for char in s:
#         result = char + result
#     return result
# print(reverse_string("hello"))
#
# def reverse_slice(s):
#     return s[::-1]
# print(reverse_slice("hello"))

# #Exercise 6
# def remove_all_occurences(sub, s):
#     if sub in s:
#         return s.replace(sub, "")
#     else:
#         return s
# print(remove_all_occurences("a", "Kamil"))

# #Exercise 7
# def s_compile(s, key):
#     alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
#     result = ""
#     for ch in s:
#         index = alphabet.find(ch.lower())
#         if index == -1:
#             result = result + ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index]
#     return result
# key = "zgçyfvbrdoştumacpğslküneöjıih"
# print(s_compile("Hello folks", key))

# #Exercise 8
# def remove_dups(s):
#     result = ""
#     for char in s:
#         if char.lower() not in result.lower():
#             result += char
#     return result
# print(remove_dups("HellLo"))
