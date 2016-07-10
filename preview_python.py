def func1():
    print("fun1 start keyword:string")
    str1 = "hello world"
    print(3*str1)
    print(str1[2:5])
    print("fun1 end")

def func2():
    print("fun2 start ")
    num = -4
    print(num)
    print(abs(num))
    print(num ** 3)
    num = 49
    print(num ** 0.5)
    print("fun2 end")

def func3():
    print("fun3 start keyword:for loop")
    sum_num1 = 0
    sum_num2 = 0
    sum_num3 = 0
    for num in range(1,10):
        print(num)
        sum_num1 = sum_num1 + num
        sum_num2 += num
        sum_num3 = num
    print("sum_num1 =", sum_num1)
    print("sum_num2 =", sum_num2)
    print("sum_num3 =", sum_num3)
    print("fun3 end")

def func4():
    print("fun4 start keyword:list")
    list1 = ["I","Like","NTUST"]
    # 新手入門版
    for i in range(3):
        print("index =", i, " = ", list1[i])
    # 進階版
    for index,item in enumerate(list1):
        print("index =", index, " = ", item)
    list1.append("台科資工營好好玩!!! ")
    #show again
    for index,item in enumerate(list1):
        print("index =", index, " = ", item)
    print(list1[3] * 5)
    print("fun4 end")

def boss():
    print("boss start keyword: if condition / list-comprehensions / Built-in Functions")
    flags = [False,False,False]
    for i in range(3):
        print ("i =", i)
        flags[i] = True
        print(flags)
        if all(flags):
            list1 = [x for x in range(10) if x % 2 == 1]
            print(list1)
            print(sum(list1))
    print("boss end")

if __name__ == '__main__':
    func1()
    print("------------next----------")
    func2()
    print("------------next----------")
    func3()
    print("------------next----------")
    func4()
    print("------------next----------")
    boss()