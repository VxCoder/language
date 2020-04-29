import ply.lex as lex
from ply.lex import LexToken


tokens = [
    'STRING', 
    'ASSIGN_CONTENT',      # 定义需求
    'RE_ASSIGN',           # 指定需求
    'ASSIGN_DEVELOP',      # 指定开发
    'DEFINE_REQ',          # 定义需求
    'END',                 # 结束符
    'SHOW_REQ',            # 看需求详情
]

t_END = "[。.]"

def t_DEFINE_REQ(t: LexToken):
    r"(我有个需求(叫做)?)|(我又要提个需求(叫做)?)"
    return t

def t_RE_ASSIGN(t: LexToken):
    r"让我们回到需求"
    return t

def t_SHOW_REQ(t: LexToken):
    r"让我看看需求"
    return t

def t_ASSIGN_CONTENT(t: LexToken):
    r"内容(改)?为"
    return t

def t_ASSIGN_DEVELOP(t: LexToken):
    r'开发我选'
    return t 


def t_STRING(t: LexToken):
    r'\w+'
    return t


t_ignore = ' \t'
def t_newline(t: LexToken):
    r'\n'
    t.lexer.lineno += len(t.value)

def t_COMMENT(t):
    r'\#.*'

def t_error(t: LexToken):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

def get_lexer():
    return lex.lex()


def main():
    lexer = lex.lex()

    data = """
    物流重构内容为啥也不做。
    """
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)


if __name__ == "__main__":
    main()
