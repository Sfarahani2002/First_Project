print(all([1,2,3,4,5]))
print(all([0,2,3,4,5]))
numbers = [ 2, 4, 6, 7]

print(all([num % 2 == 0 for num in numbers ]))


# filter
# all
# any.py

numbers2 = [ 0, 0, 0, 0]
print(any(numbers2)) # == false
numbers2 = [ 0, 0, 1, 0] #== true

print(any([num % 2 != 0 for num in numbers]))