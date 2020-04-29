import ply.lex as lex
from ply.lex import LexToken



tokens = [
    'NOUN',   # 名词
    'VERB',   # 动词
    'END',  # 结束符
] 


t_NOUN = "(黄彬|需求)"
t_VERB = "(改|删|变|提)"
t_END = "[。.]"

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
    黄彬改需求
    """
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)


if __name__ == "__main__":
    main()
