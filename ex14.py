from sys import argv

scprit, user_name = argv
prompt = '>'

print(f"Hi {user_name}, I'm the {scprit} scprit.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

# 同理，此处运行需要输入 python ex14.py Monica
# 将提示符promte固定为>，这样后面不需要重复在input输入不同字符串了，也可将>换成 请输入：
# input内的输入可以是任意字符串
