# Project Robin

### Description
Project Robin is a project based on the development of a compiler for a robot that will move in a 10x10 grid. The robot uses a special grammar that allows it to follow a series of instructions, these instructions include movements ('MOV') and turns ('TURN') with angles of 90°, 180°, 270°, and 360°. Additionally, error handling has been incorporated to return an illegal instruction message when the movement leads the robot outside the boundaries of the grid.

### Language
The language used by the robot must be polite and must follow the grammar provided.
Here are some examples of valid sentences:

| Inputs | Instruction|
| :--- | :--- |
| Robot please move 2 steps  | MOV,2  |
| Robin kindly rotate 90 degrees | TURN,90  |
| Robot kindly rotate 270 degrees to the left | TURN,270  |
| Robot kindly move 3 steps | MOV,3  |
| Robot please turn 90 degrees to the left then move 5 units to the front then turn 180 degrees then move 2 steps to the left  | TURN,90
MOV,5
TURN,180
MOV,2  |

### Context Free Grammar
Lex
```
⟨ROBOT⟩ -> robot | Robot | ROBOT | Robin
⟨KIND⟩ -> please | kindly
⟨ROTATION⟩ -> rotate | turn | spin
⟨NUM⟩ -> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
⟨DEG⟩ -> 90 | 180 | 270 | 360
⟨TO⟩ -> to
⟨THE⟩ -> the
⟨FRONT_BACK⟩ -> front | back
⟨RIGHT_LEFT⟩ -> right | left
⟨MOVEMENT⟩ -> move | go | travel
⟨DEGREES⟩ -> degrees
⟨UNIT⟩ -> steps | units
⟨COMMA⟩ -> ,
⟨FCNCTR⟩ -> finally | lastly | last | last | and then | and finally | and lastly | and last | and
⟨NEX⟩ -> next | then | after that | afterwards | after | subsequently | successively 
⟨EOS⟩ -> \n
```

Yacc
```

```

### Simulator 

### Tools
- Python
- Lex
- Yacc

### Developers
- [Jorge Esteban Madrigal Ramírez - A01641409](https://github.com/JEMadrigal)
- [Jorge Germán Wolburg Trujillo - A01640826](https://github.com/Neuvax)
- [Ingrid Michelle González Mendoza - A01641116](https://github.com/imichglez)
