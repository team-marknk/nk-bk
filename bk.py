<<<<<<< HEAD
#hihi
print(1)
=======
import random

def generate_num(): #4자리수 숫자 생성
    dig = list(range(10))
    random.shuffle(dig)
    num = dig[:4]
    return num


def check_and_guess(guess,num):
    # 입력한 숫자(guess), 생성된 숫자(num) 비교해서 결과 출력
    if guess == num:
        print('정답')
        return True
    else:
        result = []
        for i in range(4):
            if guess[i] == num[i]:
                result.append('bulls')
            elif guess[i] in num:
                result.append('cows')
        if result:
            print(', '.join(result))
        else:
            print('out')
        return False

if __name__ == '__main__':
    print('4자리 숫자를 맞춰보세요.')
    num = generate_num()
    while True:
        guess_str = input('숫자를 입력하세요(종료를 원하시면 s를 입력해주세요.) : ')
        if guess_str.lower() == 's': # 사용자가 s를 입력하면 종료
            break
        guess = [int(d) for d in guess_str if d.isdigit()]
        if len(guess) !=4:
            print('4자리 숫자를 입력하세요.')
            continue
        if check_and_guess(guess, num):
            break


>>>>>>> fetch_HEAD

