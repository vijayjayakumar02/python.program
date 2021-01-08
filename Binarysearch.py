pos = -1


def search(lst, data):
    l = 0
    u = len(lst) - 1
    while l <= u:
        mid = (l+u) // 2
        if lst[mid] == data:
            globals()['pos'] = mid
            return True
        else:
            if lst[mid] < data:
                l = mid + 1
            else:
                u = mid - 1
    return False


a = list(map(int, input().strip().split()))
n = int(input())
if search(a, n):
    print('Found @ position: ', pos + 1)
else:
    print('Not Found')