# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


# def print_hi(name):
#     # 在下面的代码行中使用断点来调试脚本。
#     print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。
#
#
# # 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     print_hi('PyCharm')

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
class Mark:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.landmark = []


person = Person(name='qiuqiu', age=18)
# person.landmark.append(10, 20)
mark1 = Mark(x=10, y=20)
mark2 = Mark(x=30, y=50)
mark3 = Mark(x=40, y=60)
person.landmark.append(mark1)
person.landmark.append(mark2)
person.landmark.append(mark3)

for i, lm in enumerate(person.landmark):
    print(i, lm.x, lm.y)