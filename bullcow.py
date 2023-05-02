import random

def game():

    q_num = ""

    for i in range(4):
        q_num += str(random.randint(0,9))

    is_right = 0
    count = 0

    while is_right==0:

        a_num = str(input('Input 4 numbers: '))

        bull = 0
        cow = 0
        if count == 10:
            print('10회안에 맞추지 못하셨습니다.')
            exit()
        if q_num == a_num:
            print('4 bulls!!, Congratulation!!!')
            is_right = 1
        else:
            for a in a_num:
                if a in q_num:
                    if q_num.index(a) == a_num.index(a):
                        bull += 1
                    elif q_num.index(a) != a_num.index(a):
                        cow += 1

            print(f'{bull} bulls, {cow} cows')
            count += 1

        if count == 10:
            print('10회안에 맞추지 못하셨습니다.')
            exit()

game()

