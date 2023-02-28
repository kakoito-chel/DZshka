# def f( s,c,m):
#     if s >= 129: return c%2 == m%2
#     if c == m: return 0
#     h = [f(s+1, c+1, m), f(s+2, c+1, m)]
#     return any(h) if (c+1) % 2 == m % 2 else all(h)
#
# for s in range(1,128+1):
#     for m in range(1, 128+1):
#         if f(s, 0, m) == 1:
#             print(s,m)




#27802
def f(x, h):
    if h == 3 and x >= 68:
        return 1
    elif h == 3 and x < 68:
        return 0
    elif x >= 68 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)
        else:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)

for x in range(1, 68):
    if f(x, 1) == 1:
        print(x)
        break
#27803
def f(x, h):
    if h == 4 and x >= 68: 
        return 1
    elif h == 4 and x < 68:
        return 0
    elif x >= 68 and h < 4:
        return 0
    else:
        if h % 2 != 0:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)   # стратегия победителя
        else:
            return f(x + 1, h + 1) and f(x + 4, h + 1) and f(x * 5, h + 1)  # стратегия проигравшего
 
for x in range(1, 68):
    if f(x, 1) == 1:
        print(x)
  
#27804
Исключим стратегию Вани, которая позволит ему гарантированно выиграть первым ходом:
 
def f(x, h):
    if (h == 3 or h == 5) and x >= 68:
        return 1
    elif h == 5 and x < 68:
        return 0
    elif x >= 68 and h < 5:
        return 0
    else:
        if h % 2 == 0:
            return f(x + 1, h + 1) or f(x + 4, h + 1) or f(x * 5, h + 1)   # стратегия победителя
        else:
            return f(x + 1, h + 1) and f(x + 4, h + 1) and f(x * 5, h + 1)  # стратегия проигравшего
 
def f1(x, h):
    if h == 3 and x >= 68:
        return 1
    elif h == 3 and x < 68:
        return 0 
    elif x >= 68 and h < 3:
        return 0
    else:
        if h % 2 == 0:
            return f1(x + 1, h + 1) or f1(x + 4, h + 1) or f1(x * 5, h + 1)   # стратегия победителя
        else:
            return f1(x + 1, h + 1) and f1(x + 4, h + 1) and f1(x * 5, h + 1)  # стратегия проигравшего(любой ход)
 
for x in range(1, 68):
    if f(x, 1) == 1:
        print(x)
print("====")
for x in range(1, 68):
    if f1(x, 1) == 1:
        print(x)  # Исключим эти значения из списка выше        
