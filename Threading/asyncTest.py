import time

async def get_date_from_db(counter):
    data = []
    print("参数counter: ", counter)
    for i in range(counter):
        time.sleep(1)
        data.append(i)
    return data

obj = get_date_from_db(5)
print("异步函数的返回值：", obj)

try:
    obj.send(None)
except Exception as e:
    print(e)
