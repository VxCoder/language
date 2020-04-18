import ply.lex as lex
from ply.lex import LexToken

states = (
    ("string", "exclusive"),
)

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
    'START',
    'END',
    'CONTENT'

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
t_string_ignore = ''

def t_START(t:LexToken):
    r'"'
    t.lexer.code_start = t.lexer.lexpos
    t.lexer.begin('string')


def t_string_END(t:LexToken):
    r'"'
    t.value = t.lexer.lexdata[t.lexer.code_start: t.lexer.lexpos-1]
    t.type = "STRING_LITERAL"
    t.lexer.begin('INITIAL')
    return t

def t_string_newline(t: LexToken):
    r'\n'
    t.lexer.lineno += len(t.value)

def t_string_CONTENT(t:LexToken):
    r'[^"]+'


def t_string_error(t:LexToken):
    print(f"error {t.lexer.lexdata[t.lexer.lexpos]}")
    t.lexer.skip(1)


def t_IDENTIFIER(t: LexToken):
    r'[A-Za-z_][A-Za-z_0-9]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t


def t_DOUBLE_LITERAL(t:LexToken):
    r'[0-9]+\.[0-9]'
    t.value = float(t.value)
    return t

def t_INT_LITERAL(t:LexToken):
    r'[1-9][0-9]*|0'
    t.value = int(t.value)
    return t


def t_newline(t: LexToken):
    r'\n'
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
 11 222.0 if else "what func.\t"a
    """
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)


if __name__ == "__main__":
    main()
