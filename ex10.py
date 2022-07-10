tabby_cat = "\tI'm tabbed in." #\t代表Tab，即该行缩进8个空格
persian_cat = "I'm split\non a line." #此处\n代表换行，python优先默认\后的n有含义
backslash_cat = "I'm \\ a \\ cat." #此处输出结果为I'm \ a \ cat.

fat_cat= """
I'll do a list:
\t* Cat_food
\t* Fishies
\t* Catnip\n\t* Grass
""" #\t 代表Tab键，即该行缩进8个空格

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print("\a")
print("\b","c")
print("\f","c")

# python中\的转移字符和功能
# \\ 代表 反斜杠（\）
# \' 代表 单引号(')
# \" 代表 双引号(")
# \a 代表 ASCII响铃符(BEL)，即在powershell中会发出响声
# \b 代表 ASCII退格符(BS)，即往后退一格的意思
# \f 代表 ASCII进纸符(FF)，即跳页的意思
# \n 代表 ASCII换行符 (LF)，即换一行的意思
# \N{name} 代表 Unicode数据库中的字符名，其中name是它的名字，仅Unicode，看不懂？后面也是
# \r 代表 ASCII回车符(CR)，即代表删除前面字符的意思
# \t 代表 ASCII水平制表符 (TAB)
# \uxxxx 代表 值为16位 十六进制值xxxx的字符
# \Uxxxxxxxx 代表 值为32位十六进制值xxxxxxxx的字符
# \v 代表 ASCII垂直制表符(VT)
# \ooo 代表 值为八进制值ooo的字符
# \xhh 代表 值为十六进制值hh的字符
