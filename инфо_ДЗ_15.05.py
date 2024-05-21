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
    
n = int('105', 8) + (5 * 37 + 15) * int('1011', 3) ** int('BA', 15)
nn = F(n, 24)
ans = 0
for i in nn:
    if i == 'H':
        ans += 1
print(ans)
