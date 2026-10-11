name1 = input('Enter name1:')
name2 = input('Enter name2:')
name3 = input('Enter name3:')

score1 = int(input('score:'))
score2 = int(input('score:'))
score3 = int(input('score:'))

a = [name1, name2, name3]
b = [score1, score2, score3]

for name, score in zip(a, b):
    if score >= 50:
        print(name, 'pass')
    else:
        print(name, 'fail')
