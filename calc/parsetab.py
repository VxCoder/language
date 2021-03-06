
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD DIV DOUBLE_LITERAL LP MUL RP SUBexpression : term\n                 | expression ADD term\n                 | expression SUB term\n    term : primary_expression\n            | term MUL primary_expression\n            | term DIV primary_expression\n    primary_expression : DOUBLE_LITERAL\n                          | LP expression RP\n                          | SUB primary_expression\n    '
    
_lr_action_items = {'DOUBLE_LITERAL':([0,3,6,7,8,9,10,],[5,5,5,5,5,5,5,]),'LP':([0,3,6,7,8,9,10,],[6,6,6,6,6,6,6,]),'SUB':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,],[3,8,-1,3,-4,-7,3,3,3,3,3,-9,8,-2,-3,-5,-6,-8,]),'$end':([1,2,4,5,11,13,14,15,16,17,],[0,-1,-4,-7,-9,-2,-3,-5,-6,-8,]),'ADD':([1,2,4,5,11,12,13,14,15,16,17,],[7,-1,-4,-7,-9,7,-2,-3,-5,-6,-8,]),'RP':([2,4,5,11,12,13,14,15,16,17,],[-1,-4,-7,-9,17,-2,-3,-5,-6,-8,]),'MUL':([2,4,5,11,13,14,15,16,17,],[9,-4,-7,-9,9,9,-5,-6,-8,]),'DIV':([2,4,5,11,13,14,15,16,17,],[10,-4,-7,-9,10,10,-5,-6,-8,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,6,],[1,12,]),'term':([0,6,7,8,],[2,2,13,14,]),'primary_expression':([0,3,6,7,8,9,10,],[4,11,4,4,4,15,16,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> term','expression',1,'p_expression','calc_yacc.py',7),
  ('expression -> expression ADD term','expression',3,'p_expression','calc_yacc.py',8),
  ('expression -> expression SUB term','expression',3,'p_expression','calc_yacc.py',9),
  ('term -> primary_expression','term',1,'p_term','calc_yacc.py',21),
  ('term -> term MUL primary_expression','term',3,'p_term','calc_yacc.py',22),
  ('term -> term DIV primary_expression','term',3,'p_term','calc_yacc.py',23),
  ('primary_expression -> DOUBLE_LITERAL','primary_expression',1,'p_primary_expression','calc_yacc.py',35),
  ('primary_expression -> LP expression RP','primary_expression',3,'p_primary_expression','calc_yacc.py',36),
  ('primary_expression -> SUB primary_expression','primary_expression',2,'p_primary_expression','calc_yacc.py',37),
]
