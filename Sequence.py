# 索引 从0开始
greeting = 'Hello'
# 从左到右
print(greeting[0])
print(greeting[1])
print(greeting[2])
# 从右到左
print('-------------------')
print(greeting[-1])
print(greeting[-2])
print(greeting[-3])
number = [1,2,3,4,5,6,7,8,9,10]
print(number[1:3]) # 取索引为第一和第二
print(number[-3:-1]) # 取索引为倒数第三和倒数第二的元素
# 变量【a：b】 （a <= x  <b）
print(number[-3:])
print(number[:])
print(number[10:0])
# 步长
print(number[0:10:2])
# 序列相加
print([1,2,3] + [4,5,6])
a = [1,2]
b = [5,6]
print(a + b)
s = 'hello,'
w = 'world'
print(s + w)
print('hello,' * 5)
print([7] * 10)
jj = 'hello,world'
print('w' in jj)
# in运算符用于检验某种条件是否成真
users = ['xiangming','xiaozhi','xiaoxiao']
print('xiaomeng' in users)
# len()   max()   min()
numbers = [300,200,100,800,500]
print(len(numbers))
print(max(numbers))
print(max(10,99,88,77))
print(min(7,0,-1,3))

# 列表的更新，赋值，增加，及删除
aw = [1,2,3,4,5]
aw[1] = 10
print(aw)
tring = [None] * 5
tring[3] = 'test'
print(tring)
tring1 = [1,2,3]
tring1.append(4)
print(tring1)
tring1.append('test')
print(tring1)
ssw = ['a','b','c']
ssw.append(3) # 添加数字
print(ssw)