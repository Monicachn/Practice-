types_of_people = 10
x = f"There are {types_of_people} types of people."

bianary = "bianary"
do_not = "don't"
y = f"Those who know {bianary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = "False"
joke_evaluation = "Isn't that joke so fuuny?!{}" #{}此处理解为占位符

print(joke_evaluation.format(hilarious)) # .format函数可以占位符内容替换成（）内的值

w = "This is the left side of..."
e = "a string with a ritht side."

print(w + e)
