# Project Robin

## Description
Project Robin is a project based on the development of a compiler for a robot that will move in a 10x10 grid. The robot uses a special grammar that allows it to follow a series of instructions, these instructions include movements ('MOV') and turns ('TURN') with angles of 90°, 180°, 270°, and 360°. Additionally, error handling has been incorporated to return an illegal instruction message when the movement leads the robot outside the boundaries of the grid.

## CPU Automaton
This project involves a deterministic automaton that simulates the movement logic of a robot in a 2D matrix of 10 blocks. The automaton is represented using a directed graph using the Graphviz library, allowing for a clear visualization of the different states and transitions between them. Furthermore, a method is included to execute a sequence of instructions and determine if they have been successfully completed or if there are missing instructions. Our project provides a basic implementation of the automaton and can be customized and expanded upon to meet specific needs.<br>
<p align="center">
<img width="449" alt="Captura de pantalla 2023-05-31 a la(s) 14 28 59" src="https://github.com/Neuvax/ProjectRobin/assets/114161329/c8e0d4c8-3101-4f86-a8c8-29ee13d550fe">
</p>

## Lex Analyzer
The lexical analyzer has the objective of scanning the source code of the program in search of lexical units or tokens, which are the basic components of the programming language. These tokens can include keywords, identifiers, constants, operators, symbols, and other elements that are part of the language.<br>This language must be created in order to make communication with the robot possible and the language must be polite. For a sentence to be valid, Robot or Robin must be entered, followed by a kind word and the desired instruction.
For the creation of valid sentence variants, ChatGPT was used.<br>
**Lex**<br>
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
### Language
**Here are some examples of valid sentences:**

| Inputs | Instruction|
| :--- | :--- |
| Robot please move 2 steps  | MOV,2  |
| Robin kindly rotate 90 degrees | TURN,90  |
| Robot kindly rotate 270 degrees to the left | TURN,270  |
| Robot kindly move 3 steps | MOV,3  |
| Robot please turn 90 degrees to the left then move 5 units to the front<br> then turn 180 degrees then move 2 steps to the left  | TURN,90<br>MOV,5<br>TURN,180<br>MOV,2  |

**Examples of invalid sentences:**<br>
`Robot move 5 steps quickly`<br>
`Robin rotate 90 degrees right now`<br>
`ROBOT moves 3 units`<br>
`robot turn 270 degrees`<br>

## Context Free Grammar
The Yacc file contains the grammar specification of the generated language in the form of production rules. Used with Lex to perform parsing. The Yacc-generated parser validates the structure of the source code against these rules and builds a parse tree if the code is valid.

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
- EOS<br>

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

## Simulator 
For the test of our robot it is necessary to enter a valid sentence, as output the instructions will be generated. In this way the cpu will print the addresses that were generated.

#### Input 
```
Robin please move 5 steps then turn 90 degrees and finally move 9 steps
```
#### Output
```
MOV,5 
TURN,90
MOV,9
```
#### Starting point
```
→ - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
```
```
- - - - - → - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
```
#### End point
```
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - - - - - -
- - - - - ↓ - - - -
```

## Tools
- Python
- Lex
- Yacc

## Testing
In order to test our robot, you need to be located in the `cpu.py` file found in the CPU folder and run the command `python3 cpu.py` <br>
When executing the command, an `.asm` file is also created indicating whether the sentences that were entered are valid or not.
If valid, a **PASS** will appear, otherwise the program will stop.<br>

On the other hand, in the **Test** folder there is a file called `test.py`, which does the unit test of the robot.py code (which would be the robot's cpu) to check that the turns are being performed correctly.

It is important to mention that we have to install 3 things as prerequesite for the program to work:

* A lex compiler; we use flex 2.6.4
* A Yacc compiler; we use bison 2.3
* A Python compiler; we use Python 3

## Developers
- [Esteban Madrigal](https://github.com/JEMadrigal)
- [Jorge Wolburg](https://github.com/Neuvax)
- [Ingrid González](https://github.com/imichglez)
