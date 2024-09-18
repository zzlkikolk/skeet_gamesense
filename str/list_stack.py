# list 模拟stack(栈)
"""
压入（Push）: 将一个元素添加到栈的顶端。
弹出（Pop）: 移除并返回栈顶元素。(最末尾)
查看栈顶元素（Peek/Top）: 返回栈顶元素而不移除它。
检查是否为空（IsEmpty）: 检查栈是否为空。
获取栈的大小（Size）: 获取栈中元素的数量。
"""


def list_stack() -> None:
    stack = [0]
    # push
    stack.append(1)
    stack.append(2)
    index = 0
    while index < len(stack):
        # 获取最末尾元素
        num = stack.pop()
        print(num)
        index += 1


if __name__ == '__main__':
    list_stack()
