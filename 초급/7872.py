# 7872. 톱니바퀴

import math

a, b, c = map(int, input().split())     # 톱니 개수

print(math.ceil(c*10 / a))  # c가 10바퀴 돌기 위해 a가 돌아야 하는 최소 횟수