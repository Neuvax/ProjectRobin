# Context Free Grammar

This Yacc file contains the grammar specification of the generated language in the form of production rules. Used with Lex to perform parsing. The Yacc-generated parser validates the structure of the source code against these rules and builds a parse tree if the code is valid.

Compiler constraints:

- Compiler must be in LEX and YACC.
- Compiler must read the sentence from a file.
- Compiler must generate a file: `instructions.asm` with the list of instructions.<br>
For example:
```
MOV,2
TURN,270
```
Tokens:

- ROBOT 
- KIND 
- ROTATION 
- NUM
- DEG
- TO 
- THE 
- FRONT_BACK 
- RIGHT_LEFT 
- MOVEMENT 
- DEGREES 
- UNIT 
- COMMA 
- FCNCTR 
- NEX 
- EOS

**Yacc**
```
⟨program⟩ -> ⟨sentence_list⟩
             | ⟨program⟩ ⟨EOS⟩ ⟨program⟩
             
⟨sentence_list⟩ -> ⟨ROBOT⟩ ⟨sentence⟩
                   | ⟨sentence_list⟩ ⟨sentence⟩
                   
⟨sentence⟩ -> ⟨action_list⟩
              | ⟨KIND⟩ ⟨sentence⟩
             
⟨action_list⟩ -> ⟨action⟩
                 | ⟨action⟩ ⟨FCNCTR⟩ ⟨action_list⟩
                 | ⟨action⟩ ⟨NEX⟩ ⟨action_list⟩
                 
⟨action⟩ -> ⟨rotation_action⟩
            | ⟨movement_action⟩
              
⟨rotation_action⟩ -> ⟨ROTATION⟩ ⟨distance⟩ ⟨DEGREES⟩
                     | ⟨ROTATION⟩ ⟨distance⟩ ⟨DEGREES⟩ ⟨TO⟩ ⟨THE⟩ ⟨RIGHT_LEFT⟩
              
⟨movement_action⟩ -> ⟨MOVEMENT⟩ ⟨distance⟩ ⟨UNIT⟩
                     | ⟨MOVEMENT⟩ ⟨distance⟩ ⟨UNIT⟩ ⟨FRONT_BACK⟩
                     | ⟨MOVEMENT⟩ ⟨distance⟩ ⟨UNIT⟩ ⟨RIGHT_LEFT⟩
                     | ⟨MOVEMENT⟩ ⟨distance⟩ ⟨UNIT⟩ ⟨TO⟩ ⟨THE⟩ ⟨RIGHT_LEFT⟩
                     | ⟨MOVEMENT⟩ ⟨distance⟩ ⟨UNIT⟩ ⟨TO⟩ ⟨THE⟩ ⟨FRONT_BACK⟩
                 
⟨distance⟩ -> ⟨NUM⟩
              | ⟨DEG⟩
```
