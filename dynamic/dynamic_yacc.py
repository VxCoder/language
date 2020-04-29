import ply.yacc as yacc

from dynamic_lex import tokens, get_lexer


def p_translation_unit(p):
    '''translation_unit : definition_or_statement
        | translation_unit definition_or_statement
    '''
    pass

def p_definition_or_statement(p):
    '''definition_or_statement : function_definition
        | statement
    '''
    pass


def p_function_definition(p):
    '''function_definition : FUNCTION IDENTIFIER LP parameter_list RP block
        | FUNCTION IDENTIFIER LP RP block
    '''
    pass

def p_parameter_list(p):
    '''
    parameter_list : IDENTIFIER
        | parameter_list COMMA IDENTIFIER
    '''
    pass


def p_statement(p):
    '''statement : expression SEMICOLON
        | global_statement
        | if_statement
        | while_statement
        | for_statement
        | return_statement
        | break_statement
        | continue_statement
    '''
    pass


def p_global_statement(p):
    """GLOBAL_T identifier_list SEMICOLON"""
    pass

def p_identifier_list(p):
    """ identifier_list : IDENTIFIER
        | identifier_list COMMA IDENTIFIER
    """
    pass

def p_if_statement(p):
    """if_statement
        : IF LP expression RP block
        | IF LP expression RP block ELSE block
        | IF LP expression RP block elsif_list
        | IF LP expression RP block elsif_list ELSE block
    """
    pass

def p_elsif_list(p):
    """ elsif_list: elsif
        | elsif_list elsif
    """
    pass

def p_elsif(p):
    """elsif: ELSIF LP expression RP block
    """
    pass

def  p_while_statement(p):
    """while_statement: WHILE LP expression RP block
    """
    pass

def p_for_statement(p):
    """for_statement: FOR LP expression_opt SEMICOLON expression_opt SEMICOLON expression_opt RP block
    """
    pass

def p_expression_opt(p):
    '''expression_opt: /* empty */
        | expression
    '''
    pass

def p_return_statement(p):
    '''return_statement: RETURN_T expression_opt SEMICOLON
    '''
    pass

def p_break_statement(p):
    '''break_statement: BREAK SEMICOLON'''
    pass

def p_continue_statement(p):
    '''continue_statement: CONTINUE SEMICOLON
    '''
    pass

def p_statement_list(p):
    '''statement_list : statement
        | statement_list statement
    '''
    pass

def p_expression(p):
    '''expression : IDENTIFIER ASSIGN expression
        | logical_or_expression
    '''
    pass

def p_logical_or_expression(p):
    '''logical_or_expression: logical_and_expression
        | logical_or_expression LOGICAL_OR logical_and_expression
    '''
    pass

def p_logical_and_expression(p):
    '''logical_and_expression: equality_expression
        | logical_and_expression LOGICAL_AND equality_expression
    '''
    pass


def p_equality_expression(p):
    '''equality_expression: relational_expression
        | equality_expression EQ relational_expression
        | equality_expression NE relational_expression
    '''
    pass

def p_relational_expression(p):
    '''relational_expression: additive_expression
        | relational_expression GT additive_expression
        | relational_expression GE additive_expression
        | relational_expression LT additive_expression
        | relational_expression LE additive_expression
    '''
    pass

def p_block(p):
    '''block: LC statement_list RC
        | LC RC
    '''
    pass

# argument_list
#         : expression
#         {
#             $$ = crb_create_argument_list($1);
#         }
#         | argument_list COMMA expression
#         {
#             $$ = crb_chain_argument_list($1, $3);
#         }
#         ;



# additive_expression
#         : multiplicative_expression
#         | additive_expression ADD multiplicative_expression
#         {
#             $$ = crb_create_binary_expression(ADD_EXPRESSION, $1, $3);
#         }
#         | additive_expression SUB multiplicative_expression
#         {
#             $$ = crb_create_binary_expression(SUB_EXPRESSION, $1, $3);
#         }
#         ;
# multiplicative_expression
#         : unary_expression
#         | multiplicative_expression MUL unary_expression
#         {
#             $$ = crb_create_binary_expression(MUL_EXPRESSION, $1, $3);
#         }
#         | multiplicative_expression DIV unary_expression
#         {
#             $$ = crb_create_binary_expression(DIV_EXPRESSION, $1, $3);
#         }
#         | multiplicative_expression MOD unary_expression
#         {
#             $$ = crb_create_binary_expression(MOD_EXPRESSION, $1, $3);
#         }
#         ;
# unary_expression
#         : primary_expression
#         | SUB unary_expression
#         {
#             $$ = crb_create_minus_expression($2);
#         }
#         ;
# primary_expression
#         : IDENTIFIER LP argument_list RP
#         {
#             $$ = crb_create_function_call_expression($1, $3);
#         }
#         | IDENTIFIER LP RP
#         {
#             $$ = crb_create_function_call_expression($1, NULL);
#         }
#         | LP expression RP
#         {
#             $$ = $2;
#         }
#         | IDENTIFIER
#         {
#             $$ = crb_create_identifier_expression($1);
#         }
#         | INT_LITERAL
#         | DOUBLE_LITERAL
#         | STRING_LITERAL
#         | TRUE_T
#         {
#             $$ = crb_create_boolean_expression(CRB_TRUE);
#         }
#         | FALSE_T
#         {
#             $$ = crb_create_boolean_expression(CRB_FALSE);
#         }
#         | NULL_T
#         {
#             $$ = crb_create_null_expression();
#         }
#         ;


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
