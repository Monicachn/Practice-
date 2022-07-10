#Here's some new strange stuff, remember type it exactlay.

days = "Mon Tue Wed Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"#\n代表换行的意思,不缩进

print("Here are the days:", days)
print("Here are the months:", months)

print("""
There's something going on here.
With the three double-quotoes.
We'll be able to type as much as we like.
Even 4 lines if want, or 5, or 6.
""") # 单字符串用“”，多行字符串要用”“” ”“”，且三个双引号之间不能有空格（单引号也可以）
# python 会把相连的俩引号认定是字符串边界，故三个引号中间引入多行不容易出错。举例

"I am 6'2 tall" #将字符串中的双引号转义
"I am 6\'2" tall.' #将字符串的单引号转义
#具体使用可以参考习题10
