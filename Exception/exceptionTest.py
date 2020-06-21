try:
    a = 2/0
except ValueError as e:
    print(e)
finally:
    print("end")

# 在捕获异常的时候，若except关键词指定的异常类型，不是实际触发的异常类型，那么就不能正常的捕获
