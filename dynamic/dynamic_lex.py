import ply.lex as lex
from ply.lex import LexToken

reserved = {
    'function': 'FUNCTION',
    'if': 'IF',
    'else': 'ELSE',
    'elsif': 'ELSIF',
    'while': 'WHILE',
    'for': 'FOR',
    'return': 'RETURN_T',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'null': 'NULL_T',
    'true': 'TRUE_T',
    'false': 'FALSE_T',
    'global': 'GLOBAL_T'
}

tokens = [
    'LP',
    'RP',
    'LC',
    'RC',
    'SEMICOLON',
    'COMMA',
    'LOGICAL_AND',
    'LOGICAL_OR',
    'ASSIGN',
    'EQ',
    'NE',
    'GT',
    'GE',
    'LT',
    'LE',
    'ADD',
    'SUB',
    'MUL',
    'DIV',
    'MOD',
    'IDENTIFIER',
    'INT_LITERAL',
    'DOUBLE_LITERAL',
    'STRING_LITERAL',
] + list(reserved.values())


t_LP = r'\('
t_RP = r'\)'
t_LC = r'{'
t_RC = r'}'
t_SEMICOLON = r';'
t_COMMA = r','
t_LOGICAL_AND = r'&&'
t_LOGICAL_OR = r'\|\|'
t_ASSIGN = r'='
t_EQ = r'=='
t_NE = r'!='
t_GT = r'>'
t_GE = r'>='
t_LT = r'<'
t_LE = r'<='
t_ADD = r'\+'
t_SUB = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_MOD = r'%'

t_ignore = ' \t'


def t_IDENTIFIER(t: LexToken):
    r'[A-Za-z_][A-Za-z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t


def t_newline(t: LexToken):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_COMMENT(t):
    r'\#.*'
    pass


def t_error(t: LexToken):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)


def get_lexer():
    return lex.lex()


def main():
    lexer = lex.lex()

    data = """
function if feifen
    """
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)


if __name__ == "__main__":
    main()
