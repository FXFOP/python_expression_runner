import sympy as sp

class PythonExpressionRunner:
    """
    模拟 QLExpress 的 Python 表达式解析器
    """

    def __init__(self):
        """
        初始化表达式运行器
        """
        self.context = {}

    def add_variable(self, name, value):
        """
        将变量添加到上下文
        :param name: 变量名
        :param value: 变量值
        """
        self.context[name] = value

    def execute(self, expression):
        """
        执行表达式
        :param expression: 要执行的表达式字符串
        :return: 执行结果或None（执行失败时）
        """
        try:
            # 将上下文中的变量替换到表达式中
            result = eval(expression, {}, self.context)
            return result
        except Exception as e:
            print(f"执行表达式失败: {e}")
            return None

    def add_function(self, name, function):
        """
        添加自定义函数
        :param name: 函数名
        :param function: 函数对象
        """
        self.context[name] = function
