def count_valleys(steps, paths):
    sum = 0
    count = 0
    for i in range(steps):
        if paths[i] == 'U':
            sum = sum + 1
        else:
            sum = sum - 1
        if sum == 0 and paths[i] == 'U':
            count += 1
    return count


steps = int(input().strip())
path = input()
print(count_valleys(steps, path))