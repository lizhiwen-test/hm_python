def sum_2_num(num1,num2):
    """对两个数字的求和 """
    result = num1 + num2

    # 可以使用返回值，告诉调用函数一方计算的结果

    return  result
    # return 表示后续代码不会被执行

# 可以使用变量，来接收函数执行的返回结果
sum_result = sum_2_num(20,30)

print("计算结果是 %d "% sum_result)