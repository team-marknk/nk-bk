import random

q_num = ""

for i in range(4):
    q_num += str(random.randint(0,9))

a_num = int(input('Input 4 numbers: '))

if (len(str(a_num)) <= 3) | (len(str(a_num)) >= 5):
    print('4자리 숫자를 입력해주세요.')

print(a_num)

