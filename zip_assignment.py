name1 = input('Enter name 1:')
name2 = input('Enter name 2:')
name3 = input('Enter name 3:')
print(name1, name2, name3)
score1 = int(input('first_score:'))
score2 = int(input('second_score:'))
score3 = int(input('third_score:'))
a = [ name1, name2, name3 ]
b = [ score1, score2, score3]
print(list(zip(a, b)))

if score1 >= 50:
    print('pass')
else:
    print('fail')

if score2 >= 50:
    print('pass')
else:
    print('fail')

if score3 >= 50:
    print('pass')
else:
    print('fail')
