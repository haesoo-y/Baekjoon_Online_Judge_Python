x, y, w, h = map(int,input().split())
North = h - y
South = y - 0
West = x - 0
East = w - x
lst = [North, South, West, East]
# print(lst)
# [1, 2, 6, 4]
print(min(lst))