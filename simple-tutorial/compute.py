# 1. 运算符
# abs 绝对值 
# int 转为int
# float 转为float
print(pow(2, 5))

# 7*7*7*7 的写法
print(7*7*7*7)
print(pow(7, 4))
print(7**4)
a = 7
for i in range(3):
    a *= 7
print(a)

# if else
# python 用 elif 代替 else if
test_a = 234
if test_a < 100:
    print('<100')
elif test_a < 500:
    print('<500')
else:
    print('other')


# for 循环
print(list(range(12)))
# 前闭后开
print(list(range(7, 12)))
# 5 表示步长
print(list(range(7, 12, 2)))

for i in range(2, 14, 3):
    print(i)

# break 中断循环
for i in range(10):
    print(i)
    if i > 5:
        break

# continue 中断本次循环,进行下一次循环
for i in range(10):
    if i == 5:
        continue
    print(i)

# pass 语句什么都不做，是为了保证程序结构的完整性