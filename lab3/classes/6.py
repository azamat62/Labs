def prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
def filtr(lst):
    result = list(filter(lambda x: prime(x), lst))
    print(result)

n = int(input())
lst = []
for i in range(n):
    x = int(input())
    lst.append(x)

filtr(lst)


