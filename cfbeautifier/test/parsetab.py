
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\t;\x14\xcc\x8a;\x92\xb2\x16\xb1;S\xbeM<\xb8'
    
_lr_action_items = {'BODY':([0,3,4,6,7,11,13,26,32,75,76,77,],[-67,5,-21,5,-20,-23,-24,-26,-32,-81,-31,-37,]),'IDSYNTAX':([5,8,9,10,14,15,16,22,23,27,28,37,38,40,41,42,44,50,51,52,53,55,56,64,65,67,68,69,70,71,72,73,74,75,79,85,86,87,88,90,98,99,100,105,106,107,110,111,113,114,115,116,119,121,124,126,127,129,],[-9,15,-8,15,15,-13,15,-6,15,-5,15,-38,-29,15,-7,-27,15,-10,15,-80,-28,-30,-82,-75,-4,-76,-74,-11,15,-78,-3,-77,-73,-81,-67,-83,15,-65,-66,-2,-67,-12,15,15,-67,-67,15,-55,-67,-67,-64,15,-48,15,15,-49,-67,-45,]),'SEMICOLON':([15,36,56,64,65,66,67,68,69,71,72,73,74,75,79,85,87,88,89,90,98,106,107,111,113,114,115,116,117,118,119,121,125,126,127,128,129,],[-13,52,-82,-75,-4,-67,-76,-74,-11,-78,-3,-77,-73,-81,-67,-83,-65,-66,-79,-2,-67,-67,-67,-55,-67,-67,-64,-47,52,52,-48,-67,-67,-49,-67,-50,-45,]),'SYMBOL':([22,27,50,51,70,86,99,100,105,110,124,],[-6,-5,-10,69,69,69,-12,69,69,69,69,]),'BUNDLE':([0,3,4,6,7,11,13,26,32,75,76,77,],[-67,9,-21,9,-20,-23,-24,-26,-32,-81,-31,-37,]),'CLASS':([27,28,37,38,40,41,42,47,48,52,53,55,62,78,80,81,82,83,84,102,122,123,],[-5,41,-38,-29,41,-7,-27,-67,-70,-80,-28,-30,41,-68,-42,-40,-69,-39,41,-43,-72,-71,]),'OPEN_BRACE':([15,18,19,20,21,24,25,34,49,50,51,56,57,99,100,124,],[-13,-67,-67,-51,27,27,-67,-67,-18,-10,27,-82,-19,-12,27,27,]),'OPEN_PAREN':([15,18,19,63,65,68,69,71,74,92,93,96,],[-13,22,22,22,-4,-53,-11,-54,-52,-53,-54,-52,]),'COMMA':([15,22,23,27,29,30,31,56,58,64,65,66,67,68,69,70,71,72,73,74,75,79,85,86,91,92,93,94,95,96,97,98,103,106,107,111,112,115,127,],[-13,-6,-15,-5,44,-16,-14,-82,-17,-75,-4,90,-76,-74,-11,-61,-78,-3,-77,-73,-81,-67,-83,-61,-57,-58,-59,-60,-62,-56,105,-67,110,90,90,-55,-63,-64,90,]),'QSTRING':([22,27,37,41,47,48,50,51,52,62,70,78,80,81,82,83,84,86,99,100,102,105,110,122,123,124,],[-6,-5,-38,-7,-67,-70,-10,72,-80,72,72,-68,-42,-40,-69,-39,72,72,-12,72,-43,72,72,-72,-71,72,]),'ARROW':([72,79,],[-3,99,]),'CLOSE_BRACE':([15,27,33,37,38,40,41,42,45,46,47,48,52,53,54,55,56,59,60,61,62,65,69,70,72,78,80,81,82,83,84,85,87,88,91,92,93,94,95,96,97,101,102,104,105,108,112,115,122,123,],[-13,-5,-34,-38,-29,-67,-7,-27,-35,-67,-67,-70,-80,-28,75,-30,-82,-36,75,-33,-41,-4,-11,-61,-3,-68,-42,-40,-69,-39,-67,-83,-65,-66,-57,-58,-59,-60,-62,-56,-67,-67,-43,75,-2,-44,-63,-64,-72,-71,]),'NAKEDVAR':([22,27,50,51,70,86,99,100,105,110,124,],[-6,-5,-10,65,65,65,-12,65,65,65,65,]),'PROMISE_TYPE':([27,33,37,41,45,46,47,48,52,59,61,62,78,80,81,82,83,84,101,102,108,122,123,],[-5,48,-38,-7,-35,48,-67,-70,-80,-36,-33,-41,-68,-42,-40,-69,-39,-67,-67,-43,-44,-72,-71,]),'ASSIGN':([15,35,39,120,],[-13,50,-46,50,]),'CLOSE_PAREN':([15,22,23,29,30,31,43,56,58,65,69,72,85,86,91,92,93,94,95,96,103,109,112,115,],[-13,-6,-15,-67,-16,-14,56,-82,-17,-4,-11,-3,-83,-61,-57,-58,-59,-60,-62,-56,-67,56,-63,-64,]),'$end':([0,1,2,3,4,6,7,11,12,13,17,26,32,75,76,77,],[-67,0,-1,-22,-21,-67,-20,-23,-67,-24,-25,-26,-32,-81,-31,-37,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'bundle_statements_node':([24,],[32,]),'selection':([28,40,],[36,36,]),'semicolon':([36,117,118,],[53,122,123,]),'class_expression':([28,40,62,84,],[37,37,37,37,]),'constraint_id':([28,40,116,121,],[35,35,120,120,]),'maybe_comma':([66,97,106,107,127,],[89,104,113,114,129,]),'promise_line':([62,84,],[81,81,]),'bundle_statement':([33,46,],[45,59,]),'body_token':([3,6,],[8,8,]),'promiser_statement':([62,84,],[78,78,]),'comma':([66,97,106,107,127,],[88,88,88,88,88,]),'litems_node':([63,],[85,]),'usefunction':([51,70,86,100,105,110,124,],[73,94,94,73,94,94,73,]),'id':([8,10,14,16,23,28,40,44,51,70,86,100,105,110,116,121,124,],[14,16,18,19,31,39,39,31,74,96,96,74,96,96,39,39,74,]),'aitems_node':([18,19,],[21,24,]),'specification':([0,],[1,]),'rval':([51,100,124,],[66,107,127,]),'promisee_statement':([62,84,],[82,82,]),'nakedvar':([51,70,86,100,105,110,124,],[71,93,93,71,93,93,71,]),'bodyattribs':([28,],[40,]),'aitem':([23,44,],[30,58,]),'symbol':([51,70,86,100,105,110,124,],[68,92,92,68,92,92,68,]),'empty':([20,],[25,]),'body':([3,6,],[4,4,]),'aitems':([23,],[29,]),'blocks_node':([0,],[2,]),'constraints_node':([113,114,],[117,118,]),'blocks':([3,],[6,]),'string':([51,62,70,84,86,100,105,110,124,],[64,79,91,79,91,64,91,91,64,]),'classpromise':([62,84,],[80,102,]),'bodyattrib':([28,40,],[38,55,]),'classpromises_node':([47,],[61,]),'bundle':([3,6,],[7,7,]),'open_brace':([21,24,51,100,124,],[28,33,70,70,70,]),'open_paren':([18,19,63,],[23,23,86,]),'bundle_statements':([33,],[46,]),'close_brace':([54,60,104,],[76,77,111,]),'litem':([70,86,105,110,],[95,95,112,112,]),'class':([28,40,62,84,],[42,42,83,83,]),'close_paren':([43,109,],[57,115,]),'classpromises':([62,],[84,]),'none':([0,6,12,18,19,25,29,34,40,46,47,66,79,84,97,98,101,103,106,107,113,114,121,125,127,],[3,12,17,20,20,34,43,49,54,60,62,87,98,101,87,106,108,109,87,87,116,116,125,128,87,]),'constraint':([116,121,],[119,126,]),'bodyattribs_node':([21,],[26,]),'list':([51,100,124,],[67,67,67,]),'promise_type':([33,46,],[47,47,]),'functionid':([51,70,86,100,105,110,124,],[63,63,63,63,63,63,63,]),'litems':([70,86,],[97,103,]),'arrow':([79,],[100,]),'bundle_token':([3,6,],[10,10,]),'assign':([35,120,],[51,124,]),'block':([3,6,],[11,13,]),'constraints':([116,],[121,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> specification","S'",1,None,None,None),
  ('specification -> blocks_node','specification',1,'p_specification','/vagrant/cfbeautifier/parse.py',22),
  ('comma -> COMMA','comma',1,'p__comma_COMMA_string_QSTRING_nakedvar_NAKEDVAR_open_brace_OPEN_BRACE_open_paren_OPEN_PAREN_class_expression_CLASS_bundle_token_BUNDLE_body_token_BODY_assign_ASSIGN_symbol_SYMBOL_arrow_ARROW_id_IDSYNTAX','/vagrant/cfbeautifier/parse.py',197),
  ('string -> QSTRING','string',1,'p__comma_COMMA_string_QSTRING_nakedvar_NAKEDVAR_open_brace_OPEN_BRACE_open_paren_OPEN_PAREN_class_expression_CLASS_bundle_token_BUNDLE_body_token_BODY_assign_ASSIGN_symbol_SYMBOL_arrow_ARROW_id_IDSYNTAX','/vagrant/cfbeautifier/parse.py',198),
  ('nakedvar -> NAKEDVAR','nakedvar',1,'p__comma_COMMA_string_QSTRING_nakedvar_NAKEDVAR_open_brace_OPEN_BRACE_open_paren_OPEN_PAREN_class_expression_CLASS_bundle_token_BUNDLE_body_token_BODY_assign_ASSIGN_symbol_SYMBOL_arrow_ARROW_id_IDSYNTAX','/vagrant/cfbeautifier/parse.py',199),
  ('open_brace -> OPEN_BRACE','open_brace',1,'p__comma_COMMA_string_QSTRING_nakedvar_NAKEDVAR_open_brace_OPEN_BRACE_open_paren_OPEN_PAREN_class_expression_CLASS_bundle_token_BUNDLE_body_token_BODY_assign_ASSIGN_symbol_SYMBOL_arrow_ARROW_id_IDSYNTAX','/vagrant/cfbeautifier/parse.py',200),
  ('open_paren -> OPEN_PAREN','open_paren',1,'p__comma_COMMA_string_QSTRING_nakedvar_NAKEDVAR_open_brace_OPEN_BRACE_open_paren_OPEN_PAREN_class_expression_CLASS_bundle_token_BUNDLE_body_token_BODY_assign_ASSIGN_symbol_SYMBOL_arrow_ARROW_id_IDSYNTAX','/vagrant/cfbeautifier/parse.py',201),
  ('class_expression -> CLASS','class_expression',1,'p__comma_COMMA_string_QSTRING_nakedvar_NAKEDVAR_open_brace_OPEN_BRACE_open_paren_OPEN_PAREN_class_expression_CLASS_bundle_token_BUNDLE_body_token_BODY_assign_ASSIGN_symbol_SYMBOL_arrow_ARROW_id_IDSYNTAX','/vagrant/cfbeautifier/parse.py',202),
  ('bundle_token -> BUNDLE','bundle_token',1,'p__comma_COMMA_string_QSTRING_nakedvar_NAKEDVAR_open_brace_OPEN_BRACE_open_paren_OPEN_PAREN_class_expression_CLASS_bundle_token_BUNDLE_body_token_BODY_assign_ASSIGN_symbol_SYMBOL_arrow_ARROW_id_IDSYNTAX','/vagrant/cfbeautifier/parse.py',203),
  ('body_token -> BODY','body_token',1,'p__comma_COMMA_string_QSTRING_nakedvar_NAKEDVAR_open_brace_OPEN_BRACE_open_paren_OPEN_PAREN_class_expression_CLASS_bundle_token_BUNDLE_body_token_BODY_assign_ASSIGN_symbol_SYMBOL_arrow_ARROW_id_IDSYNTAX','/vagrant/cfbeautifier/parse.py',204),
  ('assign -> ASSIGN','assign',1,'p__comma_COMMA_string_QSTRING_nakedvar_NAKEDVAR_open_brace_OPEN_BRACE_open_paren_OPEN_PAREN_class_expression_CLASS_bundle_token_BUNDLE_body_token_BODY_assign_ASSIGN_symbol_SYMBOL_arrow_ARROW_id_IDSYNTAX','/vagrant/cfbeautifier/parse.py',205),
  ('symbol -> SYMBOL','symbol',1,'p__comma_COMMA_string_QSTRING_nakedvar_NAKEDVAR_open_brace_OPEN_BRACE_open_paren_OPEN_PAREN_class_expression_CLASS_bundle_token_BUNDLE_body_token_BODY_assign_ASSIGN_symbol_SYMBOL_arrow_ARROW_id_IDSYNTAX','/vagrant/cfbeautifier/parse.py',206),
  ('arrow -> ARROW','arrow',1,'p__comma_COMMA_string_QSTRING_nakedvar_NAKEDVAR_open_brace_OPEN_BRACE_open_paren_OPEN_PAREN_class_expression_CLASS_bundle_token_BUNDLE_body_token_BODY_assign_ASSIGN_symbol_SYMBOL_arrow_ARROW_id_IDSYNTAX','/vagrant/cfbeautifier/parse.py',207),
  ('id -> IDSYNTAX','id',1,'p__comma_COMMA_string_QSTRING_nakedvar_NAKEDVAR_open_brace_OPEN_BRACE_open_paren_OPEN_PAREN_class_expression_CLASS_bundle_token_BUNDLE_body_token_BODY_assign_ASSIGN_symbol_SYMBOL_arrow_ARROW_id_IDSYNTAX','/vagrant/cfbeautifier/parse.py',208),
  ('aitem -> id','aitem',1,'p_aitem_id','/vagrant/cfbeautifier/parse.py',197),
  ('aitems -> <empty>','aitems',0,'p_aitems_','/vagrant/cfbeautifier/parse.py',197),
  ('aitems -> aitem','aitems',1,'p_aitems_aitem','/vagrant/cfbeautifier/parse.py',197),
  ('aitems -> aitems COMMA aitem','aitems',3,'p_aitems_aitems_COMMA_aitem','/vagrant/cfbeautifier/parse.py',197),
  ('aitems_node -> none empty none none','aitems_node',4,'p_aitems_node_none_empty_none_none','/vagrant/cfbeautifier/parse.py',197),
  ('aitems_node -> open_paren aitems none close_paren','aitems_node',4,'p_aitems_node_open_paren_aitems_none_close_paren','/vagrant/cfbeautifier/parse.py',197),
  ('block -> bundle','block',1,'p_block_bundle_body','/vagrant/cfbeautifier/parse.py',197),
  ('block -> body','block',1,'p_block_bundle_body','/vagrant/cfbeautifier/parse.py',198),
  ('blocks -> <empty>','blocks',0,'p_blocks_','/vagrant/cfbeautifier/parse.py',197),
  ('blocks -> block','blocks',1,'p_blocks_block','/vagrant/cfbeautifier/parse.py',197),
  ('blocks -> blocks block','blocks',2,'p_blocks_blocks_block','/vagrant/cfbeautifier/parse.py',197),
  ('blocks_node -> none blocks none none','blocks_node',4,'p_blocks_node_none_blocks_none_none','/vagrant/cfbeautifier/parse.py',197),
  ('body -> body_token id id aitems_node bodyattribs_node','body',5,'p_body_body_token_id_id_aitems_node_bodyattribs_node','/vagrant/cfbeautifier/parse.py',197),
  ('bodyattrib -> class','bodyattrib',1,'p_bodyattrib_class_selection_semicolon','/vagrant/cfbeautifier/parse.py',197),
  ('bodyattrib -> selection semicolon','bodyattrib',2,'p_bodyattrib_class_selection_semicolon','/vagrant/cfbeautifier/parse.py',198),
  ('bodyattribs -> bodyattrib','bodyattribs',1,'p_bodyattribs_bodyattrib','/vagrant/cfbeautifier/parse.py',197),
  ('bodyattribs -> bodyattribs bodyattrib','bodyattribs',2,'p_bodyattribs_bodyattribs_bodyattrib','/vagrant/cfbeautifier/parse.py',197),
  ('bodyattribs_node -> open_brace bodyattribs none close_brace','bodyattribs_node',4,'p_bodyattribs_node_open_brace_bodyattribs_none_close_brace','/vagrant/cfbeautifier/parse.py',197),
  ('bundle -> bundle_token id id aitems_node bundle_statements_node','bundle',5,'p_bundle_bundle_token_id_id_aitems_node_bundle_statements_node','/vagrant/cfbeautifier/parse.py',197),
  ('bundle_statement -> promise_type classpromises_node','bundle_statement',2,'p_bundle_statement_promise_type_classpromises_node','/vagrant/cfbeautifier/parse.py',197),
  ('bundle_statements -> <empty>','bundle_statements',0,'p_bundle_statements_','/vagrant/cfbeautifier/parse.py',197),
  ('bundle_statements -> bundle_statement','bundle_statements',1,'p_bundle_statements_bundle_statement','/vagrant/cfbeautifier/parse.py',197),
  ('bundle_statements -> bundle_statements bundle_statement','bundle_statements',2,'p_bundle_statements_bundle_statements_bundle_statement','/vagrant/cfbeautifier/parse.py',197),
  ('bundle_statements_node -> open_brace bundle_statements none close_brace','bundle_statements_node',4,'p_bundle_statements_node_open_brace_bundle_statements_none_close_brace','/vagrant/cfbeautifier/parse.py',197),
  ('class -> class_expression','class',1,'p_class_class_expression','/vagrant/cfbeautifier/parse.py',197),
  ('classpromise -> class','classpromise',1,'p_classpromise_class_promise_line','/vagrant/cfbeautifier/parse.py',197),
  ('classpromise -> promise_line','classpromise',1,'p_classpromise_class_promise_line','/vagrant/cfbeautifier/parse.py',198),
  ('classpromises -> <empty>','classpromises',0,'p_classpromises_','/vagrant/cfbeautifier/parse.py',197),
  ('classpromises -> classpromise','classpromises',1,'p_classpromises_classpromise','/vagrant/cfbeautifier/parse.py',197),
  ('classpromises -> classpromises classpromise','classpromises',2,'p_classpromises_classpromises_classpromise','/vagrant/cfbeautifier/parse.py',197),
  ('classpromises_node -> none classpromises none none','classpromises_node',4,'p_classpromises_node_none_classpromises_none_none','/vagrant/cfbeautifier/parse.py',197),
  ('constraint -> constraint_id assign rval maybe_comma','constraint',4,'p_constraint_constraint_id_assign_rval_maybe_comma','/vagrant/cfbeautifier/parse.py',197),
  ('constraint_id -> id','constraint_id',1,'p_constraint_id_id','/vagrant/cfbeautifier/parse.py',197),
  ('constraints -> <empty>','constraints',0,'p_constraints_','/vagrant/cfbeautifier/parse.py',197),
  ('constraints -> constraint','constraints',1,'p_constraints_constraint','/vagrant/cfbeautifier/parse.py',197),
  ('constraints -> constraints constraint','constraints',2,'p_constraints_constraints_constraint','/vagrant/cfbeautifier/parse.py',197),
  ('constraints_node -> none constraints none none','constraints_node',4,'p_constraints_node_none_constraints_none_none','/vagrant/cfbeautifier/parse.py',197),
  ('empty -> <empty>','empty',0,'p_empty_','/vagrant/cfbeautifier/parse.py',197),
  ('functionid -> id','functionid',1,'p_functionid_id_symbol_nakedvar','/vagrant/cfbeautifier/parse.py',197),
  ('functionid -> symbol','functionid',1,'p_functionid_id_symbol_nakedvar','/vagrant/cfbeautifier/parse.py',198),
  ('functionid -> nakedvar','functionid',1,'p_functionid_id_symbol_nakedvar','/vagrant/cfbeautifier/parse.py',199),
  ('list -> open_brace litems maybe_comma close_brace','list',4,'p_list_open_brace_litems_maybe_comma_close_brace','/vagrant/cfbeautifier/parse.py',197),
  ('litem -> id','litem',1,'p_litem_id_string_symbol_nakedvar_usefunction','/vagrant/cfbeautifier/parse.py',197),
  ('litem -> string','litem',1,'p_litem_id_string_symbol_nakedvar_usefunction','/vagrant/cfbeautifier/parse.py',198),
  ('litem -> symbol','litem',1,'p_litem_id_string_symbol_nakedvar_usefunction','/vagrant/cfbeautifier/parse.py',199),
  ('litem -> nakedvar','litem',1,'p_litem_id_string_symbol_nakedvar_usefunction','/vagrant/cfbeautifier/parse.py',200),
  ('litem -> usefunction','litem',1,'p_litem_id_string_symbol_nakedvar_usefunction','/vagrant/cfbeautifier/parse.py',201),
  ('litems -> <empty>','litems',0,'p_litems_','/vagrant/cfbeautifier/parse.py',197),
  ('litems -> litem','litems',1,'p_litems_litem','/vagrant/cfbeautifier/parse.py',197),
  ('litems -> litems COMMA litem','litems',3,'p_litems_litems_COMMA_litem','/vagrant/cfbeautifier/parse.py',197),
  ('litems_node -> open_paren litems none close_paren','litems_node',4,'p_litems_node_open_paren_litems_none_close_paren','/vagrant/cfbeautifier/parse.py',197),
  ('maybe_comma -> none','maybe_comma',1,'p_maybe_comma_none_comma','/vagrant/cfbeautifier/parse.py',197),
  ('maybe_comma -> comma','maybe_comma',1,'p_maybe_comma_none_comma','/vagrant/cfbeautifier/parse.py',198),
  ('none -> <empty>','none',0,'p_none_','/vagrant/cfbeautifier/parse.py',197),
  ('promise_line -> promiser_statement','promise_line',1,'p_promise_line_promiser_statement_promisee_statement','/vagrant/cfbeautifier/parse.py',197),
  ('promise_line -> promisee_statement','promise_line',1,'p_promise_line_promiser_statement_promisee_statement','/vagrant/cfbeautifier/parse.py',198),
  ('promise_type -> PROMISE_TYPE','promise_type',1,'p_promise_type_PROMISE_TYPE','/vagrant/cfbeautifier/parse.py',197),
  ('promisee_statement -> string arrow rval maybe_comma constraints_node semicolon','promisee_statement',6,'p_promisee_statement_string_arrow_rval_maybe_comma_constraints_node_semicolon','/vagrant/cfbeautifier/parse.py',197),
  ('promiser_statement -> string none none maybe_comma constraints_node semicolon','promiser_statement',6,'p_promiser_statement_string_none_none_maybe_comma_constraints_node_semicolon','/vagrant/cfbeautifier/parse.py',197),
  ('rval -> id','rval',1,'p_rval_id_symbol_string_list_usefunction_nakedvar','/vagrant/cfbeautifier/parse.py',197),
  ('rval -> symbol','rval',1,'p_rval_id_symbol_string_list_usefunction_nakedvar','/vagrant/cfbeautifier/parse.py',198),
  ('rval -> string','rval',1,'p_rval_id_symbol_string_list_usefunction_nakedvar','/vagrant/cfbeautifier/parse.py',199),
  ('rval -> list','rval',1,'p_rval_id_symbol_string_list_usefunction_nakedvar','/vagrant/cfbeautifier/parse.py',200),
  ('rval -> usefunction','rval',1,'p_rval_id_symbol_string_list_usefunction_nakedvar','/vagrant/cfbeautifier/parse.py',201),
  ('rval -> nakedvar','rval',1,'p_rval_id_symbol_string_list_usefunction_nakedvar','/vagrant/cfbeautifier/parse.py',202),
  ('selection -> constraint_id assign rval maybe_comma','selection',4,'p_selection_constraint_id_assign_rval_maybe_comma','/vagrant/cfbeautifier/parse.py',197),
  ('semicolon -> SEMICOLON','semicolon',1,'p_semicolon_SEMICOLON_close_brace_CLOSE_BRACE_close_paren_CLOSE_PAREN','/vagrant/cfbeautifier/parse.py',197),
  ('close_brace -> CLOSE_BRACE','close_brace',1,'p_semicolon_SEMICOLON_close_brace_CLOSE_BRACE_close_paren_CLOSE_PAREN','/vagrant/cfbeautifier/parse.py',198),
  ('close_paren -> CLOSE_PAREN','close_paren',1,'p_semicolon_SEMICOLON_close_brace_CLOSE_BRACE_close_paren_CLOSE_PAREN','/vagrant/cfbeautifier/parse.py',199),
  ('usefunction -> functionid litems_node','usefunction',2,'p_usefunction_functionid_litems_node','/vagrant/cfbeautifier/parse.py',197),
]