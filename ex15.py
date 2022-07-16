from sys import argv #从软件包sys中取出argv模块

script, filename = argv #将argv解包，将所有参数依次赋值给左边的这些变量

txt = open(filename) #返回“文件对象”，not文件内容

print(f"Here's your file {filename}:") #f：格式化的输出
print(txt.read()) #读取txt的内容

print("Type the filename again:")
file_again = input('>') #提示符>，再次输入文件名

txt_again = open(file_again) #再次返回文件对象，not文件内容

print(txt_again.read()) #读取文件内容

# 同上练习题，此处运行时输入 python ex15.py ex15_sample.txt
# 其他：函数function，方法method

# 拓展
# close：关闭文件，同保存
# read：读取文件内容，也可以把结果赋给一个变量
# readline：只读取文本文件中的一行
# truncate：清空文件，请小心使用该命令
# write('stuff')：将"stuff"写入文件
# seek(0)：将读写位置移动到文件开头
