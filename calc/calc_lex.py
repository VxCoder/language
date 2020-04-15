import ply.lex as lex
from ply.lex import LexToken

tokens = (
    'ADD',
    'SUB',
    'MUL',
    'DIV',
    'DOUBLE_LITERAL',
    'LP',
    'RP'
)

t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_LP = r'\('
t_RP = r'\)'


def t_DOUBLE_LITERAL(t: LexToken):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t


def t_newline(t: LexToken):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t: LexToken):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


def get_lexer():
    return lex.lex()


def main():
    lexer = lex.lex()

    data = """
3 + 4 * 10
+ -20 * 2
    """
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)


if __name__ == "__main__":
    main()
