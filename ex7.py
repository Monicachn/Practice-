print("Mary had a little lamb.")
print("Tis fleece was white as {}.".format('snow')) #字符串需要加引号不然bug
print("And every that Mary went.")
print("." * 10) #what'd that do

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch that comma at the end. Try removing it to see what happens
print(end1 + end2 + end3 + end4 + end5 + end6,end='')
print(end7 + end8 + end9 + end10 + end11 + end12)
# print默认打印一行后换行，默认末尾是\n，用end=''代替\n，不换行
# 练习
print('小敏敏\n小敏敏')


#format用法熟悉小练习哈哈哈
a="m" * 2
b= "chunchun love {}."
print(b.format(a))
