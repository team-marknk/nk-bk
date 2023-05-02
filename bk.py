import random

def bulls_and_cows():
    print('Let\'s play Bulls and Cows game!!')
    print('If you want to quit this game, type \'exit\' whenever you want.')
    print('*'*60)
    answer = random.sample(range(1, 9+1), 4)
    input_nums = ''
    try_count = 0
    
    # For debug
    # print(answer)
    
    while answer != input_nums:
        input_ori = input('Input 4 numbers: ')
        if input_ori == 'exit':
            return 'Quit this game. byebye~'
        elif input_ori.isdigit() == False:
            print('!!!!Input 4 different nums!!!!')
            continue
        
        input_nums = [int(i) for i in input_ori]
        print(input_nums)
        if len(set(input_nums)) != 4:
            print('!!!!Input 4 different nums!!!!')
            continue

        bulls = 0
        cows = 0
        
        for index, i in enumerate(input_nums):
            if answer[index] == int(i):
                bulls += 1
            elif int(i) in answer:
                cows += 1
            else:
                pass
        print(f'Bulls={bulls}, Cows={cows}, try again!')
        print('-'*40)
        try_count += 1

    return print(f'Congratulations! you win! you tried {try_count} times!')

if __name__ == '__main__':
    bulls_and_cows()
