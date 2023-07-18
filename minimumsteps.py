def solve(x, y):
    c = 0
    q = x//y if x>y else y//x
    r = x%y if x>y else y%x
    if r == 0 and q % 2 == 0:
        q = q>>1
        while q:
            c += 1
            q = q>>1
        return c
    return -1

t = int(input())
while t:
    x = int(input())
    y = int(input())
    print(solve(x,y))
    t -= 1