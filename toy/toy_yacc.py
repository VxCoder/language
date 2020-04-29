import ply.yacc as yacc
from pydantic import BaseModel
from typing import List, Optional
from toy_lex import tokens, get_lexer

class Requirement(BaseModel):
    name: str ="" # 需求名
    content: str =""# 需求内容
    develop: str =""# 开发

SYMBOL_TABLE:List[Requirement] = {}
LATEST_SYMBOL:str = None


def p_contents(p):
    '''contents : sentence
        | contents sentence
    '''
    print(SYMBOL_TABLE)
    p[0] = ""


def p_sentence(p):
    '''sentence : define  
        | assign_content
        | assign_develop
        | re_assign  
        | show
    '''

def p_define(p):
    '''define :  DEFINE_REQ STRING END
    '''
    global LATEST_SYMBOL
    SYMBOL_TABLE[p[2]] = Requirement(name=p[2])
    LATEST_SYMBOL = p[2]

def p_show(p):
    '''show : SHOW_REQ STRING END'''
    print(SYMBOL_TABLE.get(p[2], f"哪有提过{p[2]}这个需求"))

def p_re_assign(p):
    '''re_assign : RE_ASSIGN STRING END
    '''
    global LATEST_SYMBOL

    if p[2] not in SYMBOL_TABLE:
        print(f"哪有提过{p[2]}这个需求")
        return
    LATEST_SYMBOL = p[2]

def p_assign_content(p):
    '''assign_content : ASSIGN_CONTENT STRING END
    '''
    if LATEST_SYMBOL == None:
        print("需求名都没呢")
        return
    SYMBOL_TABLE[LATEST_SYMBOL].content = p[2]

def p_assign_develop(p):
    '''assign_develop : ASSIGN_DEVELOP STRING END
    '''
    if LATEST_SYMBOL == None:
        print("需求名都没呢")
        return
    SYMBOL_TABLE[LATEST_SYMBOL].develop = p[2]


def p_error(p):
    print("Syntax error in input!")

if __name__ == "__main__":
    parser = yacc.yacc()
    test_sentence = [
        "我有个需求叫做物流重构。",
        "内容为逗你玩。",
        "开发我选姚俊超。",
        "我又要提个需求物流不重构。",
        "内容为你猜。",
        "让我们回到需求物流。",
        "让我们回到需求物流重构。",
        "内容改为支持100种物流方式。",
        "让我看看需求物流不重构。"
    ]
    # while True:
    #     try:
    #         s = input('你要说啥 >')
    #     except EOFError:
    #         break
    for s in test_sentence:
        if not s:
            continue
        print(s)
        result = parser.parse(s, lexer=get_lexer())
        print(result)
