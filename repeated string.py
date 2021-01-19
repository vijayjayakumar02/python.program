s = input()
n = int(input())
n1 = s.count('a') * (n // len(s)) + s[:(n % len(s))].count('a')
print(n1)
