# 需要传入参数
def my_function(str):
    print(str)


# 给定参数默认值
def default_value_function(str1='zhang'):
    print(str1)


# 不定参数长度
def args_function(args1, *vartuples):
    print("\n不定参数长度")
    print(args1)
    print(*vartuples)


# 指定参数类型，和返回参数
def add_function(arg1: int, arg2: int) -> int:
    return arg1 + arg2


if __name__ == '__main__':
    my_function("zhang1")
    default_value_function()
    args_function(1, 12, 23)
    print("加法{}".format(add_function(1, 2)))
