# 开始学习参数、解包和变量啦
from sys import argv #从sys模块调用argv参数变量
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variaable is:", first)
print("Your second variable is", second)
print("Your third variable is:", third)

# 解释
# 第二行import语句，是将python的特性引入脚本的意思，可以调用模块，程序小，并可查阅
# argv是参数变量，这个变量保存了运营脚本时传递给python脚本的参数。
# 第四行将argv解包，与其将所有参数放到同一个变量下面，不如将其赋值给4个变量
# 即把argv中的东西取出、解包，将所有参数依次赋值给左边的变量

#关于运行
#跟常规print运行不太一致，即运行命令为 python ex13.py first 2nd 3rd

#延申
# argv和input的用法：input表示从用户输入处获取，argv表示从其包中获取
# 命令行参数是字数串，需要用int()将其变成整数，像int(input())这样
