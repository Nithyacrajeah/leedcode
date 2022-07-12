from functools import reduce
lst = [3, 30, 34, 5, 9]
str_lst = [str(n) for n in lst]
max_lst = reduce(lambda n1, n2: (n1 + n2) if (n1 + n2) > (n2 + n1) else n2 + n1, str_lst)
print(max_lst)

# wrong


# DSA(Data structure and Algorithm)


#lst=[3,4,5,6,2]
# 2 sum pair
# 3 sum pair 9[4,3,2]
# 12 [3,4,5]
