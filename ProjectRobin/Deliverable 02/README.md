# Context Free Grammar
This repository contains a context-free grammar structure for defining robot instructions. The grammar allows you to construct valid robot commands for various actions such as rotation, movement, and more.

### Robin´s Grammar

```
⟨S⟩ -> ⟨ROBOT⟩ ⟨INSTRUCTION⟩ ⟨CONNECTOR⟩ ⟨EOS⟩ | ⟨ROBOT⟩ ⟨INSTRUCTION⟩ ⟨EOS⟩ | ⟨ROBOT⟩ ⟨INSTRUCTION⟩
  
⟨ROBOT⟩ -> "robot" | "Robot" | "ROBOT" | "Robin"
  
⟨INSTRUCTION⟩ -> ⟨KIND⟩ ⟨ACTION⟩ | ⟨ACTION⟩

⟨KIND⟩ -> "please" | "kindly" 

⟨ACTION⟩ -> ⟨ROTATION⟩ | ⟨MOVEMENT⟩ ⟨DIR⟩ | ⟨MOVEMENT⟩

⟨ROTATION⟩ -> ⟨VROTATION⟩ ⟨DEGQ⟩ "degrees" ⟨CLOCK⟩ | ⟨VROTATION⟩ ⟨DEGQ⟩ "degrees" | ⟨VROTATION⟩ ⟨DIRECT⟩

⟨VROTATION⟩ -> "rotate" | "turn" | "spin" | "revolve"

⟨DEGQ⟩ -> "90" | "180" | "270" | "360"

⟨CLOCK⟩ -> "to the" ⟨ORI2⟩ | ⟨ORI3⟩
 
⟨ORI2⟩ -> "right" | "left"

⟨ORI3⟩ -> "clockwise" | "counterclockwise" | "right" | "left"
 
⟨MOVEMENT⟩ -> ⟨VMOVEMENT⟩ ⟨DIST⟩ ⟨UNIT⟩
  
⟨VMOVEMENT⟩ -> "move" | "go" | "travel" | "proceed"

⟨DIST⟩ -> ⟨NUM⟩
 
⟨NUM⟩ -> "0" | "1" | "2" | "3" | "4" | "5"

⟨UNIT⟩ -> "steps" | "units"

⟨DIRECT⟩ -> ⟨ORI1⟩ | "to the" ⟨ORI1⟩

⟨ORI1⟩ -> "right" | "left" | "front" | "back"
  
⟨CNCTR⟩ -> ⟨COMMA⟩ | ⟨COMMA⟩ ⟨NEX⟩ ⟨INSTRUCTION⟩

⟨NEX⟩ -> "next" | "then" | "after that" | "afterwards" | "after" | "subsequently" | "successively"

⟨EOS⟩ -> ⟨COMMA⟩ ⟨FCNCTR⟩ ⟨INSTRUCTION⟩ | ⟨FCNCTR⟩ ⟨INSTRUCTION⟩ | ⟨INSTRUCTION⟩
  
⟨COMMA⟩ -> ", "
  
⟨FCNCTR⟩ -> "finally" | "lastly" | "last" | "and then" | "and finally" | "and lastly" | "and last" | "and"
```
