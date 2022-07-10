my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total= my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# 这个习题主要学习创建嵌入变量内容的字符串，即创建格式化字符串。
# 格式化字符串前缀为f（format），即在“”的字符串前+f，变量需要用{}填写
#（ps：可以把{}当成求值的意思）
# 1 = "Zed Shaw"不可行，因为1是有效变量名称，可以用a1.
