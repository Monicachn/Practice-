from sys import argv #从软件包sys中取出argv模块

script, filename = argv #将argv解包，将所有参数依次赋值给左边的这些变量

print(f"We're going to erase {filename}.") #f:格式化字符串，filename可写test.txt
print("If you don't want that, hit CTRL-C(^c).") #ctrl-c可停止运行
print("If you do want that, hit RETURN.") # return键可继续运行

input("?") #输入字符串？

print("Opening the file...")
target = open(filename, 'w')
# ‘w’是特殊字符串，用来表示文件的访问模式，代表write，文件为写入模式，同理r代表读取read
# 若open(filename)，则表示用只读模式打开filename
print("Truncating the file. Goodbye!") #truncate截断
target.truncate() #清空文件target

print("Now I'm going to ask you for three lines.")

line1 = input('line 1:')
line2 = input("line 2:")
line3 = input("line 3:")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n") # 换行
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()

# 拓展
# 可以用‘w+’、'r+'、'a+'，把文件用同时读写的方法打开，并根据使用的字符，以不一样的方式实线文件的定位
