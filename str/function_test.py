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


if __name__ == '__main__':
    my_function("zhang1")
    default_value_function()
    args_function(1,12,23)