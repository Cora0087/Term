class Course:
    def __init__(self):
        pass

    def showInfo(self):
        print("正在学习中")


class Math(Course):
    def __init__(self):
        super(Math, self).__init__()

    def showInfo(self):
        print("正在学习math中")


class AI(Course):
    def __init__(self):
        super(AI, self).__init__()
    #     pass
    #
    # def showInfo(self):
    #     print("正在学习中")


class Linux(Course):
    def __init__(self):
        super(Linux, self).__init__()

    def showInfo(self):
        print("正在学习Linux中")


class GirlFriend:
    def __init__(self, name):
        self.name = name

    def study(self, study_course):
        study_course.showInfo()


# math = Math()
# math.showInfo()
# ai = AI()
# ai.showInfo()


study_course = Linux()
girlfriend = GirlFriend("秋秋")
girlfriend.study(study_course)