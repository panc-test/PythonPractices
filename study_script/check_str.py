"""
编写程序，验证使用 input()函数输入的字符串符合我校学生学号的规则。
规则是：
（1） 共 8 个字符；
（2） 首位必须是英文大写字符；
（3） 后 7 位是数字。 若通过验证输出提示语“输入的学号是：xxxxxxxx，通过验证。”（注：“xxxxxxxx”为输 入的学号）；
    否则输出提示语“输入的学号有误，重新输入。”，并返回强制重新输入，直到输入正确的格式通过验证。

"""
while 1:
    student_id = input("输入学号：")
    if len(student_id) == 8 and student_id[0].isupper() and student_id[1:].isdigit():
        print("输入的学号是：{}，通过验证".format(student_id))
        break
    else:
        print("输入的学号有误，重新输入。")