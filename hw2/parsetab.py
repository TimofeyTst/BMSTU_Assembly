
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOL CHAR COMMA CONST DOUBLE FLOAT IDENTIFIER INT LBRACE LPAREN RBRACE RPAREN VOID\n    start : function_definition\n    \n    function_definition : return_type IDENTIFIER LPAREN parameter_list RPAREN compound_statement\n                        | return_type IDENTIFIER LPAREN RPAREN compound_statement\n    \n    return_type : VOID\n                | INT\n                | CHAR\n                | FLOAT\n                | DOUBLE\n                | BOOL\n    \n    parameter_list : parameter\n                   | parameter_list COMMA parameter\n    \n    parameter : parameter_type IDENTIFIER\n    \n    parameter_type : INT\n                   | CHAR\n                   | FLOAT\n                   | DOUBLE\n                   | BOOL\n    \n    compound_statement : LBRACE RBRACE\n    '
    
_lr_action_items = {'VOID':([0,],[4,]),'INT':([0,11,22,],[5,16,16,]),'CHAR':([0,11,22,],[6,17,17,]),'FLOAT':([0,11,22,],[7,18,18,]),'DOUBLE':([0,11,22,],[8,19,19,]),'BOOL':([0,11,22,],[9,20,20,]),'$end':([1,2,23,26,28,],[0,-1,-3,-2,-18,]),'IDENTIFIER':([3,4,5,6,7,8,9,15,16,17,18,19,20,],[10,-4,-5,-6,-7,-8,-9,25,-13,-14,-15,-16,-17,]),'LPAREN':([10,],[11,]),'RPAREN':([11,12,14,25,27,],[13,21,-10,-12,-11,]),'COMMA':([12,14,25,27,],[22,-10,-12,-11,]),'LBRACE':([13,21,],[24,24,]),'RBRACE':([24,],[28,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'function_definition':([0,],[2,]),'return_type':([0,],[3,]),'parameter_list':([11,],[12,]),'parameter':([11,22,],[14,27,]),'parameter_type':([11,22,],[15,15,]),'compound_statement':([13,21,],[23,26,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> function_definition','start',1,'p_start','main2.py',47),
  ('function_definition -> return_type IDENTIFIER LPAREN parameter_list RPAREN compound_statement','function_definition',6,'p_function_definition','main2.py',53),
  ('function_definition -> return_type IDENTIFIER LPAREN RPAREN compound_statement','function_definition',5,'p_function_definition','main2.py',54),
  ('return_type -> VOID','return_type',1,'p_return_type','main2.py',61),
  ('return_type -> INT','return_type',1,'p_return_type','main2.py',62),
  ('return_type -> CHAR','return_type',1,'p_return_type','main2.py',63),
  ('return_type -> FLOAT','return_type',1,'p_return_type','main2.py',64),
  ('return_type -> DOUBLE','return_type',1,'p_return_type','main2.py',65),
  ('return_type -> BOOL','return_type',1,'p_return_type','main2.py',66),
  ('parameter_list -> parameter','parameter_list',1,'p_parameter_list','main2.py',72),
  ('parameter_list -> parameter_list COMMA parameter','parameter_list',3,'p_parameter_list','main2.py',73),
  ('parameter -> parameter_type IDENTIFIER','parameter',2,'p_parameter','main2.py',79),
  ('parameter_type -> INT','parameter_type',1,'p_parameter_type','main2.py',85),
  ('parameter_type -> CHAR','parameter_type',1,'p_parameter_type','main2.py',86),
  ('parameter_type -> FLOAT','parameter_type',1,'p_parameter_type','main2.py',87),
  ('parameter_type -> DOUBLE','parameter_type',1,'p_parameter_type','main2.py',88),
  ('parameter_type -> BOOL','parameter_type',1,'p_parameter_type','main2.py',89),
  ('compound_statement -> LBRACE RBRACE','compound_statement',2,'p_compound_statement','main2.py',95),
]