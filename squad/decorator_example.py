# 매개변수가 있는 함수에 대한 데코레이터 정의
def emoji_decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("^~^")

    return wrapper

@emoji_decorator
def greet(name):
    print(f"안녕, {name}!")

# 데코레이터가 적용된 함수 호출
greet("saeye")
