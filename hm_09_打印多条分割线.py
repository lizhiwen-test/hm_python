def print_line(char,times):
    """ 打印单行分隔线

    :param char:分隔字符
    :param times:重复次数
"""
# char：任意字符，times：任意次数
    print(char * times)

def print_lines(char,times1):
    """打印多行分隔线

    :param char:分隔线使用的分隔字符
    :param times:分隔线重复的次数
    """
    row = 0
    while row < 5:
        print_line(char,times1)

        row += 1

print_lines("实参，",3)