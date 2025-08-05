# iterable
# iterator
# iterate

numbers = [1, 2, 3, 4, 5, 6]
color = ('red', 'green', 'blue')
nums = [1, 2, 3, 4, 5, 6]

for num in numbers:
   print(num)

# Iter()
# next()
# iterable => iter() => iterator

iterNums = iter(nums)
print(iterNums)
print(next(iterNums))
print(next(iterNums))
print(next(iterNums))
print(next(iterNums))
print(next(iterNums))
print(next(iterNums))

name = 'benifr'
iterName = iter(name)
print(next(iterName))
print(next(iterName))
print(next(iterName))
print(next(iterName))
print(next(iterName))