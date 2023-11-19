# 7884. 떨어진 숫자

drop_num = list(input())        # 떨어뜨린 숫자
pickup_num = list(input())      # 주워담은 숫자

# 떨어뜨린 숫자와 주워담은 숫자의 길이가 다르면 제대로 회수하지 못한 것이므로 NO 출력
if len(drop_num) != len(pickup_num): 
    print('NO')
    exit()

# 떨어뜨린 숫자와 주워담은 숫자 비교.
for i in drop_num:
    if i in pickup_num:
        pickup_num.remove(i)
        # print(pickup_num)

# pickup_num의 변수가 모두 지워져있으면 제대로 회수한 것이므로 YES 출력
if pickup_num:
    print('NO')
else:
    print('YES')
    