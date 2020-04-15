class Variable:

    def __init__(self):
        self.name: str = ""           # 变量名
        self.value = None             # 变量值
        self.next: Variable = None    # 下一个变量
