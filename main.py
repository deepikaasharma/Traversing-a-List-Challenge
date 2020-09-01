"""In the code cell below, write a for loop that will add the corresponding values of lst1, lst2, and lst3 together, and store them in the corresponding position in a list called output_lst.

For example:

# In
lst1 = [1, 2, 3]
lst2 = [2, 4, 6]
lst3 = [1, 3, 5]

# Result
[4, 9, 14] """

# lst1 = [1, 2, 3]
# lst2 = [2, 4, 6]
# lst3 = [1, 3, 5]

# don't change these lists
lst1 = list(range(0, 100, 4))
lst2 = list(range(1, 51, 2))
lst3 = list(range(-100, 0, 4))

# write your code below

output_lst = []
output=0

for i, val1 in enumerate(lst1):
  for j, val2 in enumerate(lst2):
    for k, val3 in enumerate(lst3):
      if i == j == k:
        output = val1+val2+val3
        output_lst.append(output)


  


print(output_lst)


