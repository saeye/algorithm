try : 
    num = input('숫자입력 : ')
    print(int(num))
except ValueError:
    print('숫자가 입력되지 않았습니다.')
