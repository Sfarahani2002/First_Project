def my_for(iterbale, func):
    iterator = iter(iterbale)

    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            func(item)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square(number):
    print(number ** 2)

my_for(numbers, square)