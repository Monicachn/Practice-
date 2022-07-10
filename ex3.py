print("I will now count my chickens:")

print("Hens", 25 + 30 / 6) #数字和运算符号之间可以不加空格，空格只是为了美观
print("Roosters", 100 - 25 * 3 % 4) # %是取余的意思，75/4，取余数3，结果为97
# line3结果为30.0，line4结果为97，前者有除数所以有浮点数，引申思考：怎么把0.25变成25%
print("Now I will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6) # %的优先级跟乘除一致，结果为6.75

print("Is it ture that 3 + 2 < 5 - 7") # “”内代表字符串，无逻辑判断

print(3 + 2 < 5 - 7) # 无引号，代表非字符串，可直接进行逻辑判断

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?",5-7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?",5 > -2) # print字符串+非引号逻辑判断时，逻辑判断能够执行
print("Is it less or equal?", 5 <= -2)
