def F(n, base):
    s = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if n == 0:
        return s[0]

    ans = []
    while n > 0:
        r = n % base
        n = n // base 
        ans.append(s[r])

    return ''.join(reversed(ans))
n = F((4**3 * 3**19), 3)    

ans = 0
for i in n:
    if i == '0':
        ans += 1
print(ans)
