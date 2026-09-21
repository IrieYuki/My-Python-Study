from student import student

call_count = {}  # 用于统计调用次数
student_list = []  # 存储所有学生对象


def call_count_func(func):
    def wrapper(*args, **kwargs):
        call_count[func.__name__] = call_count.get(func.__name__, 0) + 1
        return func(*args, **kwargs)

    return wrapper


@call_count_func
def add_student():
    number = int(input("请输入学号: "))
    name = input("请输入姓名: ")
    age = int(input("请输入年龄: "))
    scores = {
        "语文": int(input("请输入语文成绩: ")),
        "数学": int(input("请输入数学成绩: ")),
    }
    new_student = student(number, name, age, scores)
    student_list.append(new_student)
    print("添加成功！")


@call_count_func
def delete_student():
    number = int(input("请输入要删除的学生学号: "))
    for s in student_list:
        if s.number == number:
            student_list.remove(s)
            print("删除成功！")
            return
    print("未找到该学生！")


@call_count_func
def modify_student():
    number = int(input("请输入要修改的学生学号: "))
    for s in student_list:
        if s.number == number:
            s.name = input("请输入新的姓名: ")
            s.age = int(input("请输入新的年龄: "))
            s.scores["语文"] = int(input("请输入新的语文成绩: "))
            s.scores["数学"] = int(input("请输入新的数学成绩: "))
            s.average_score = sum(s.scores.values()) / len(s.scores)
            print("修改成功！")
            return
    print("未找到该学生！")


@call_count_func
def query_student():
    number = int(input("请输入要查询的学生学号: "))
    for s in student_list:
        if s.number == number:
            print(s)
            return
    print("未找到该学生！")


@call_count_func
def display_all_students():
    if not student_list:
        print("没有学生信息！")
        return
    for s in student_list:
        print(s)


@call_count_func
def save_to_file():
    with open("students.json", "w") as f:
        for s in student_list:
            f.write(
                f"{s.number},{s.name},{s.age},{s.scores['语文']},{s.scores['数学']},{s.average_score}\n"
            )
    print("保存成功！")


def load_from_file():
    print("再见！")
    print("本次操作统计:")
    for func_name, count in call_count.items():
        print(f"{func_name}: {count} 次")
