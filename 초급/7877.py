# 7877. 야바위

N, M = map(int, input().split())        # 컵의 개수, 컵이 섞인 횟수
move = []

for _ in range(M):      # 섞은 컵의 번호 
    move.append(list(map(int, input().split())))
    
A = int(input())    # 최초에 공이 들어있던 컵의 번호

# 이동한 공의 위치 저장
for a, b in move:
    if a == A:
        A = b
    elif b == A:
        A = a

print(A)    # 최종 공의 위치 출력