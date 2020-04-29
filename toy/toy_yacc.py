import ply.yacc as yacc

from toy_lex import tokens, get_lexer


def p_sentence(p):
    '''sentence : NOUN VERB NOUN END
    '''
    p[0] = f"我靠, {p[1]}又改{p[3]}"

def p_error(p):
    print("Syntax error in input!")

if __name__ == "__main__":
    parser = yacc.yacc()
    while True:
        try:
            s = input('你要说啥 >')
        except EOFError:
            break

        if not s:
            continue
        result = parser.parse(s, lexer=get_lexer())
        print(result)
