from function import (
    call_count_func,
    add_student,
    delete_student,
    modify_student,
    query_student,
    display_all_students,
    save_to_file,
    load_from_file,
)

print("""欢迎使用学生信息管理系统
1. 添加学生
2. 删除学生
3. 修改学生信息
4. 查询学生
5. 显示所有学生
6. 保存到文件
7. 退出""")

prompt = int(input("请选择操作: "))
if prompt == 1:
    add_student()
elif prompt == 2:
    delete_student()
elif prompt == 3:
    modify_student()
elif prompt == 4:
    query_student()
elif prompt == 5:
    display_all_students()
elif prompt == 6:
    save_to_file()
elif prompt == 7:
    load_from_file()
else:
    print("无效的选择！")
