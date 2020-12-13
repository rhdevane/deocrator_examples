from datetime import datetime

def not_during_the_night(func):
    print("test")
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            print("run")
            func()
        else:
            print("pass")
            pass  # Hush, the neighbors are asleep
    return wrapper

def my_decorator(func):
    print("do some other cool stuff")
    def wrapper():
        print("in wrapper")
        func()
    return wrapper
