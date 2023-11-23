# 7876. 방향 추적

N = int(input())    # 이동횟수
prev_y, prev_x = map(int, input().split())    # 첫 좌표 초기화
result = []

for _ in range(N-1):
    y, x = map(int, input().split())    # 이동좌표
    
	# y좌표 이동거리 판단
    if y != prev_y:
        if y-prev_y > 0:    # 북쪽으로 이동(1)
            result.append([1, y-prev_y])
        else:       # 남쪽으로 이동(3)
            result.append([3, prev_y-y])
	# x좌표 이동거리 판단
    else:
        if x-prev_x > 0:        # 동쪽으로 이동(2)
            result.append([2, x-prev_x])
        else:       # 서쪽으로 이동(4)
            result.append([4, prev_x-x])
            
    prev_y, prev_x = y, x       # 이동된 좌표로 초기화

# 결과 출력
for i in result:
    print(*i)