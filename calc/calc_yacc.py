import ply.yacc as yacc

from calc_lex import tokens, get_lexer


def p_expression(p):
    '''expression : term
                 | expression ADD term
                 | expression SUB term
    '''
    if len(p) == 4:
        if p[2] == '+':
            p[0] = p[1] + p[3]
        elif p[2] == '-':
            p[0] = p[1] - p[3]
    else:
        p[0] = p[1]


def p_term(p):
    '''term : primary_expression
            | term MUL primary_expression
            | term DIV primary_expression
    '''
    if len(p) == 4:
        if p[2] == '*':
            p[0] = p[1] * p[3]
        elif p[2] == '/':
            p[0] = p[1] / p[3]
    else:
        p[0] = p[1]


def p_primary_expression(p):
    '''primary_expression : DOUBLE_LITERAL
                          | LP expression RP
                          | SUB primary_expression
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = -p[2]
    else:
        p[0] = p[2]


def p_error(p):
    print("Syntax error in input!")


if __name__ == "__main__":
    parser = yacc.yacc()
    while True:
        try:
            s = input('calc >')
        except EOFError:
            break

        if not s:
            continue
        result = parser.parse(s, lexer=get_lexer())
        print(result)
