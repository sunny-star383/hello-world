# ============================================
# 简易计算器 - 从零开始看懂每一行
# ============================================

# 第一步：定义一个加法函数
# def 是 define 的缩写，意思是"定义一个函数"
# add 是函数名，后面括号里的 a 和 b 是两个输入参数
def add(a, b):
    # return 是"返回"的意思，把计算结果还给调用者
    return a + b


# 第二步：定义减法函数
def subtract(a, b):
    return a - b


# 第三步：定义乘法函数
def multiply(a, b):
    return a * b


# 第四步：定义除法函数
# 注意：除数不能为 0，所以要加一个判断
def divide(a, b):
    if b == 0:
        # 如果除数是 0，就返回错误提示
        return "错误：除数不能为 0！"
    return a / b


# 第五步：主程序入口
# 下面这个 if 的意思是：如果这个文件是直接被运行的，就执行下面的代码
# 如果这个文件是被别的文件 import 导入的，就不执行
if __name__ == "__main__":
    print("=== 简易计算器 ===")
    
    # 让用户输入两个数字
    # input() 会让程序停下来等用户输入
    # float() 把输入的文字转换成小数
    num1 = float(input("请输入第一个数字："))
    num2 = float(input("请输入第二个数字："))
    
    # 让用户选择运算
    print("\n请选择运算：")
    print("1. 加法")
    print("2. 减法")
    print("3. 乘法")
    print("4. 除法")
    
    choice = input("输入数字 1-4：")
    
    # 根据用户的选择，调用不同的函数
    if choice == "1":
        result = add(num1, num2)
        print(f"结果：{num1} + {num2} = {result}")
    elif choice == "2":
        result = subtract(num1, num2)
        print(f"结果：{num1} - {num2} = {result}")
    elif choice == "3":
        result = multiply(num1, num2)
        print(f"结果：{num1} × {num2} = {result}")
    elif choice == "4":
        result = divide(num1, num2)
        print(f"结果：{num1} ÷ {num2} = {result}")
    else:
        print("输入无效，请输入 1-4 的数字")
