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