def search(lst, data):
    for i in range(len(lst)):
        if lst[i] == data:
            return True
    return False


a = list(map(int, input().strip().split()))
n = int(input())
if search(a, n):
    print("Found")
else:
    print("Not Found")