
# /을 만나면 앞의 값 삭제
def backspace_str(input_str):
    stack = []
    __init__(self):

    self.top = None

    return answer

print(backspace_str("123//45//6789///"))



class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):
        if self.top is None:
            return None

        node = self.top
        self.top = self.top.next

        return node.item

    def is_empty(self):
        return self.top is None