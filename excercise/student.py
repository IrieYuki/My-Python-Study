class student:
    def __init__(
        self,
        number,
        name,
        age,
        scores,
    ):
        self.number = number
        self.name = name
        self.age = age

        self.average_score = sum(self.scores.values()) / len(self.scores)

    def __str__(self):
        return f"学号: {self.number}, 姓名: {self.name}, 年龄: {self.age}, 平均分: {self.average_score}"
