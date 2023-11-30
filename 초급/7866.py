# 7866. 기차와 파리

X, Y, Z = map(int, input().split())

time = X / (Y * 2) # 시간 = 거리 / 속도
distance = time * Z # 거리 = 시간 * 속도
print(int(distance))

