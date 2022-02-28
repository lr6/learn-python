print('1. int')
# 除法 得到一个浮点数
print(2 / 4)
# 除法 得到一个整数
print(5 // 4)
print(7 // 4)
print(2 // 4)
# 乘方
print(2 ** 4)
# 取余
print(17 % 3)

print('1.1 要点')
## 要点
# 1. py3 可以同时为多个变量赋值
# 2. 查看数据类型 
a, b = 2, 3
print(a ** 3)
print(type(a))

print('2. string')
str = 'hello world'
print(str.index('o'))
print(str[0])
print(str[-1])
print(str[1:4])
print(str.count('l'))
print(len(str))
print(str[::-1])
## 要点
# 1. 2存在编码问题，3不存在
# 2. 用*重复，用{}%s格式化
# 3. 两种索引方式，从左往右从0开始，从右往左从-1开始 
# 4. 字符串不可改变
# 5. 统计次数
# 6. 字符长的替换，长度

print('3. list')
ls = ['he', 100, 50, 'her']
print(type(ls))
print(ls)
print(ls + [1, 2, 3])
ls[0] = 'DC'
print(ls)
ls[2:4] = ['d', 'c']
print(ls)
ls[1:3] = []
print(ls)
ls.append('append')
print(ls)
ls.pop()
print(ls)
str2 = ';'.join(['a', 'c', 'd'])
print(str2)
print(str2.split(';')) # string 转 list

print(len(ls))
for i in ls:
    print(i)
for ind, i in enumerate(ls):
    print(ind, i)

# 要点
# 3.1 append 添加元素 
# 3.2 pop 删除元素
# 3.3 列表相加 +, extend
# 3.4 列表属于引用类型
# 3.5 值类型 字符串 元组 数值，本身不允许修改
# 3.6 引用类型 列表 字典，本身允许修改

print('4. tuple')
tup = (1, 2, 3, 4)
print(tup, type(tup), len(tup))
# 要点
# 4.1 元组的元素不可修改
# 4.2 其他与list,相同

print('5. sets')
demo_list = [1, 2, 3, 4, 1]
print(set(demo_list))
print(list(set(demo_list)))
set_a = {1, 3, 5, 7}
set_b = {1, 2, 4, 5, 6, 8, 9}
print(set_a - set_b) # 差集
print(set_b - set_a) # 差集

print(set_a | set_b) # 并集
print(set_a & set_b) # 交集
print(set_a ^ set_b) # set_a 和 set_b 不同时存在的元素
## 要点
# 5.1 无序不重复的集 
# 5.2 创建空集合 set(), 不能用 {}, 因为{}用来创建空字典

print('6. dictionaries')
dic = {} # 创建空字典
tel = { 'xm': 100, 'lm': 120, 'test': 90 }
tel2 = dict(xm = 100, lm = 120, test = 90 )
print(tel)
print(tel2)
print(tel['xm'])
# print(tel['xmm']) 报错
print(tel.get('xmm', 'null'))
del tel['test']
print(tel)
tel['new_test'] = 99
print(tel)
tel['new_test'] = 199
print(tel)
print(tel.keys())
print(tel.values())
print(sorted(tel.keys()))
print('xm' in tel)
tel.clear()
print(tel)
print('xm' not in tel)
print('test' in tel)
## 要点
# 6.1 字典是一种映射类型，它的元素是键值对
# 6.2 关键字必须使用不可变类型，list 和 tuple不能做关键字，key不可重复
# 6.3 创建空字典使用 {}
# 6.4 增加 dic['key'] = value
# 6.5 pop clear 删除
# 6.6 get() setdefault() has_keys()
# 6.7 items() 所有成员 keys() values() 