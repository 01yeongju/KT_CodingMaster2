# 7873. 전화번호 입력

s = list(input().split('-'))        # 전화열 문자번호 (형태:010-xxxx-xxxx)

for i in range(len(s)):
    if i==0:        # 첫번째 토큰 형태가 010이 아니면 유효한 형태가 아니므로 invalid 출력 후 종료
        if s[i] != '010':
            print('invalid')
            exit()
    elif i>2:       # 총 토큰 개수가 3 이상이면 유효한 형태가 아니므로 invalid 출력 후 종료
        print('invalid')
        exit()
    else:           # 각 토큰의 개수가 4 이상이며 유효한 형태가 아니므로 invalid 출력 후 종료
        if len(s[i]) != 4:
            print('invalid')
            exit()

# 유효한 형태인 경우 vaild 출력
print('valid')