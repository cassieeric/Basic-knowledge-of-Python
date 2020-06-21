class MyException(Exception):
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

def get_position(longitude=None, latitude=None):
    if longitude is None or latitude is None:
        raise MyException(longitude, latitude)

try:
    get_position()
except MyException as e:
    print("经度是：", e.longitude, "维度是：", e.latitude)
finally:
    print("end")
