def process_input():
    # 读取第一行，获取 n 和 m
    n, m = map(int, input().split())

    # 读取接下来的 n 行字符串
    expressions = [input() for _ in range(n)]

    # 创建一个字典来存储接下来的 m 对 key 和 value
    key_value_pairs = {}

    for _ in range(m):
        key, value = input().split()
        key_value_pairs[key] = value

    return expressions, key_value_pairs


def evaluate_expression(expression, context):
    # 将字段和数据替换为能够被 eval 执行的形式
    for key, value in context.items():
        value = "'{}'".format(value)
        expression = expression.replace(key, value)
    expression = expression.replace('=' ,'==')
    # 替换 AND 和 OR 为 Python 的逻辑操作符
    expression = expression.replace("AND", "and").replace("OR", "or")

# 计算表达式
    res = eval(expression)
    # print("result:", res)
    return res


# 调用函数并打印结果
expressions, key_value_pairs = process_input()
# print("Expressions:", expressions)
# print("Key-Value Pairs:", key_value_pairs)

context = key_value_pairs
for expression in expressions:
    result = evaluate_expression(expression, context)
    if result:
        print(0)
    else:
        print(1)