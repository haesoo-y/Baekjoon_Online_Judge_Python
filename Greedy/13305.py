n = int(input())
distance_lst = list(map(int, input().split()))
price_lst = list(map(int, input().split()))

min_price = price_lst[0]
result = distance_lst[0] * min_price

for i in range(1, n-1):
    min_price = min(min_price, price_lst[i])
    result += distance_lst[i] * min_price

print(result)