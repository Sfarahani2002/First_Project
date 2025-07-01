numbers_1 = [1, 2, 3, 4]# ta kamtarin tedad list joft mishan
numbers_2 = [5, 6, 7, 8, 9]
result = zip(numbers_1,numbers_2)
print(list(result)) #BADE YE BAR PRINT  badesh list khali miare
print(dict(result))

myList = [(1,3), (4,5), (8,5)]
print(list(zip(*myList)))

student = ['mohammad', 'saleh', 'fr']
midterm = [80, 85, 90]
final = [85, 90, 95]

finalGrades = [max(pair) for pair in zip(midterm,final)]
print(finalGrades)
print(list(pair for pair in zip(student,midterm,final)))
#{'mohammad':85, 'saleh':90, 'fr':95}
final_grades = {t[0]:max([t[1], t[2]]) for t in zip(student,midterm,final)}# T
print(final_grades )

final_grades_2 = zip(
    student,
    map(
        lambda pair: max(pair),
        zip(midterm,final)
    )
)
print(dict(final_grades_2))

average = zip(
    student,
    map(
        lambda pair: (pair[0] + pair[1] ) / 2,
        zip(midterm,final)
    )
)
print(dict(average))
# age faqat add bekhaym
rec = map(
        lambda pair: (pair[0] + pair[1] ) / 2,
        zip(midterm,final)
    )
print(list(rec))