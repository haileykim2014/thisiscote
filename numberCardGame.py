# n, m 을 공백으로 구분하여 입력받기
n, m = map(int,input().split())

result = 0
for i in range(n):
    # 현재 줄에서 가장 작은 수 찾기
    data = list(map(int,input().split()))
    # 가장 작은 수 들 중에서 가장 큰 수 찾기
    min_value = min(data)
    result = max(result,min_value)
# 정답 출력
print(result)