from variable import Variable
from function_define import FunctionDefine
from statements import Statements


class Interpreter:

    def __init__(self):
        self.interpreter_storage = None
        self.execute_storage = None
        self.variables: Variable = None
        self.functions: FunctionDefine = None
        self.statements: Statements = None
        self.current_line_number: int = 0


if __name__ == "__main__":
    Interpreter()
