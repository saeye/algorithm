def deco(func):
    def wrapper():
        func()
        print("^~^")

    return wrapper


@deco
def hello():
    print("Hello")

hello()


