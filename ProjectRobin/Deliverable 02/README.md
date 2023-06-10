# Lex Analyzer

The lexical analyzer has the objective of scanning the source code of the program in search of lexical units or tokens, which are the basic components of the programming language. These tokens can include keywords, identifiers, constants, operators, symbols, and other elements that are part of the language.<br>This language must be created in order to make communication with the robot possible and the language must be polite. For a sentence to be valid, Robot or Robin must be entered, followed by a kind word and the desired instruction.
For the creation of valid sentence variants, ChatGPT was used.

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
