# Yacc

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
