num1 = 1
str1 = 10
print(type(float(num1)))
print(float(num1))

print(float(str1))

print(type(str(num1)))

list1 = [10, 20, 30]
print(tuple(list1))

t1 = (100, 200, 300)
print(list(t1))

str2 = '1'
str3 = '1.1'
str4 = '[1000, 2000, 3000]'
str5 = '(1000, 2000, 3000)'
print(type(eval(str2)))
print(type(eval(str3)))
print(type(eval(str4)))
print(type(eval(str5)))