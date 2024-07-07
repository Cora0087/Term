### 关键点检测

'''python
class Mark:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass
class Person:
    # 对象初始化的时候就会被调用
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.landmark = []
        pass


### 关键点检测plus
#
'''

'''
案例1： 人体关键点描述
基本版本:
人有姓名、年龄。还有很多的关键点landmark,
每个关键点我们只需要在平面(x, y)进行描述
要求:
创建三个关键点添加到landmark， 遍历每一个元素
类: Person
name
age
# 多个关键点
landmark = []

plus版本:
现在需要区分，左右手，还有左右眼关键点
Hand:
    情况1:
    left_hand_landmark = []
    right_hand_landmark = []
    情况2:
    type='right'
    landmark = []
plus++版本:
扩展练习:
Finger:
    type
    landmark = []
Hand:
    情况1:
    left_hand_landmark = []
    right_hand_landmark = []
    情况2:
    type='right'
    fingers = []
'''


class Mark:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Hand:
    def __init__(self):
        self.type = 'left'  # 默认左手
        self.landmark = []  # 关键点


class Eye:
    def __init__(self):
        self.type = 'left'
        self.landmark = []


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.landmark = []
        self.hand = []
        self.eyes = []
# 分别创建两只手left_hand right_hand 分别添加到对应手的关键点 landmark。
# 然后再把left_hand right_hand添加到perosn.hands即可


left_eye = Eye()
left_eye.type = 'left'
left_mark1 = Mark(10, 50)
left_mark2 = Mark(10, 50)
left_eye.landmark.append(left_mark1)
left_eye.landmark.append(left_mark2)
right_eye = Eye()
right_eye.type = 'right'
right_mark1 = Mark(100, 50)
right_mark2 = Mark(200, 50)
# 添加关键点
right_eye.landmark.append(right_mark1)
right_eye.landmark.append(right_mark2)
person = Person('球球', 18)
# 添加眼
person.eyes.append(left_eye)
person.eyes.append(right_eye)
# 作业: 需求需要同学们能够遍历眼部的关键点
for eye in person.eyes:
    print(f"{eye.type} eye landmarks:")
    for landmark in eye.landmark:
        print(f"({landmark.x}, {landmark.y})")



### JSON

#python
"""
json格式
1.语法格式
key:value
2. 表示对象
{"name“: "球球"}
2. 多个数据之间使用逗号隔开
{
    "name“: "球球",
    "age" : 18
}
3. 描述多个元素使用数组
[
    {
        "name“: "球球",
        "age" : 18
    },
    {
        "name“: "球球",
        "age" : 18
    }
]
请关键点描述的基本版本使用json格式描述完成.
"""

'''{
    "name": "球球",
    "age": 18,
    "eyes": [
        {
            "type": "left",
            "landmarks": [
                {"x": 10, "y": 50},
                {"x": 20, "y": 60}
            ]
        },
        {
            "type": "right",
            "landmarks": [
                {"x": 100, "y": 50},
                {"x": 200, "y": 50}
            ]
        }
    ]
}'''
