## Testing
In order to test our robot, you need to be located in the `cpu.py` file found in the CPU folder and run the command `python3 cpu.py` <br>
When executing the command, an `.asm` file is also created indicating whether the sentences that were entered are valid or not.
If valid, a **PASS** will appear, otherwise the program will stop.<br>

On the other hand, in the **Test** folder there is a file called `test.py`, which does the unit test of the robot.py code (which would be the robot's cpu) to check that the turns are being performed correctly.

It is important to mention that we have to install 3 things as prerequesite for the program to work:

* A lex compiler; we use flex 2.6.4
* A Yacc compiler; we use bison 2.3
* A Python compiler; we use Python 3
