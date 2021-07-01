import sys
input = sys.stdin.readline

def is_pseudo(word, left, right):
    while (left < right):
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else :
            return 2
    return 1

def is_palindrome(word, left, right):
    while (left < right):
        if (word[left] == word[right]):
            left += 1
            right -= 1
        else:
            first_check = is_pseudo(word,left+1,right)
            second_check = is_pseudo(word,left,right-1)
            return min(first_check, second_check)
    return 0

n = int(input())
for _ in range(n):
    string = input().strip()
    print(is_palindrome(string, 0, len(string)-1))