def Sm(*ns):
     a = 0
     n = 0
     for i in ns:
          a += int(i)
          n += 1
     a = a / n
     return a
print(Sm(1,2,3))
