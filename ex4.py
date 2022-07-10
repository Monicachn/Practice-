cars = 100 # =的作用是为数据（数值、字符串等）取名
space_in_a_car = 4.0 #注意此处用的浮点数，去掉后，但是除输出会变成浮点数，其他无浮点数
drivers = 30 # 引申，=代表右边的值赋给左边的变量名，==代表检查左右值是否相等
passsengers = 90 # =的两边可以不加空格，但这种写法不好，不易阅读
cars_not_driven = cars-drivers # _是下划线字符
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passsengers / cars_driven


print("There are",cars,"cars available.") #数字结果为100
print("There are only",drivers,"drivers available.") #数字结果为30
print("There will be",cars_not_driven,"empty cars today.") #数字结果为70
print("We can trasnsport",carpool_capacity,"people today.") #数字结果为120.0
print("We have",passsengers,"to carpool today.") #数字结果为90
print("We need to put about",average_passengers_per_car,"in each car.") #3.0
# 倒着读代码可以更好的进行比对
# 可以将浮点数四舍五入，比如
a=round(1.7333)
print(a) #输出结果为 2
# 引申思考：如何保留一位or两位小数？
b=round(1.7333,2)
print(b) #输出结果为1.73
