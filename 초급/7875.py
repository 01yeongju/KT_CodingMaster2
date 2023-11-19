# 7875. 선물

# 최대공약수 구하는 함수수
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def max_children_gifts(gift_counts):
    # 선물 종류의 개수
    n = len(gift_counts)

    # 선물 종류별 최대공약수 초기화
    gcd_value = gift_counts[0]
    
    # 선물 종류별 최대공약수 계산
    for i in range(1, n):
        gcd_value = gcd(gcd_value, gift_counts[i])

    return gcd_value

# 입력 받기
N = int(input())
gift_counts = list(map(int, input().split()))

# 선물을 받게 되는 아이들의 최대 명수 계산
result = max_children_gifts(gift_counts)

# 결과 출력
print(result)
