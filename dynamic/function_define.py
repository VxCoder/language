from enum import Enum
from block import Block
from parameters import Parameters


class FunctionDefineType(Enum):
    USER_DEFINE_FUNC = 1   # 用户函数
    NATIVE_DEFINE_FUNC = 2  # 内置函数


class FunctionDefine:

    def __init__(self):
        self.name: str = ""  # 函数名
        self.type: FunctionDefineType = None  # 函数类型
        self.params: Parameters = None   # 参数定义(用户定义函数字段)
        self.block: Block = None    # 函数体(用户定义函数字段)
        self.proc = None     # 内置函数字段
        self.next: FunctionDefine = None  # 调用链表
