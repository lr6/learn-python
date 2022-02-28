# 异常

# 函数
def add(a, b):
    print(a + b)
    return (a + b)

res = add(6, 7)
print(res)

# 英镑和公斤的转换
def lb2kg(lb):
    return lb * 0.453

def kg2lb(kg):
    return kg * 2.204

print(lb2kg(15))
print(kg2lb(25))

# string 翻转
print('abc'[::-1])
