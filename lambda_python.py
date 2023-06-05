
# ## define function without name --> anonymous function ==> closure

l = [4,6,7,345,56]

# def get_even(num):
#     if num %2==0:
#         return True
#     return  False
#
#
# even_numbers = filter(get_even, l)
# print(list(even_numbers))
#
# print(get_even(44))

even_numbers = filter(lambda num: num%2==0, l)
print(list(even_numbers))

