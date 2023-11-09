# 7865. 채터링

N, K = map(int, input().split())        # N:입력하는 문자열 길이, K:채터링 횟수
word = input()  # 입력문자열
result = '' # 채터링 후 문자열열

for i in word:
    result += i*K   # 채터링 횟수만큼 문자 반복복
    
print(result)

'''
5 3
ABCDE       >   AAABBBCCCDDDEEE

3 2
JJH     >   JJJJHH
'''