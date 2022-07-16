print("How old are you?",end='') #end='',即告诉print不用换行符结束这一行跑到下一行
age = input() # input即接收来自用户的键入，返回字符串格式str
print("How tall are you?", end='')
height = input()
print("How much do you weigh?", end='')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
#print(f"")中的f主要作用是格式化字符串，加上f，{变量/表达式}就可以正常使用了

#输出结果为
# How old are you? 键入1
# How tall are you? 键入2
# How much do you weigh? 键入3
# So, you're 键入1 old, 键入2 tall and 键入3 heavy.

#延申，怎么用input中的字符串进行计算
# x=int(input()),int即把字数串转换成整数
