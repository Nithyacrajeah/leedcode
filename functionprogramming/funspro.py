from functools import reduce
lst=[10,2,30,4,5,6,7]

gt_ten=list(filter(lambda n:n>10,lst))
print(gt_ten)

evens=list(filter(lambda n:n>10,lst))
print(evens)

sum=reduce(lambda n1,n2:n1+n2,lst)
print(sum)

all_product=reduce(lambda n1,n2:n1*n2,lst)
print(all_product)

max_num=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(max_num)

minimum=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst)
print(minimum)