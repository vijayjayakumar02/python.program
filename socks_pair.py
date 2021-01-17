def count_pair(socks):
    pairs = 0
    for items in set(socks):
        pairs += socks.count(items) // 2
    return pairs


lst = list(map(int, input().strip().split()))
print(count_pair(lst))
