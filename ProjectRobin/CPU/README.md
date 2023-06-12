# CPU automata and simulator

This project involves a deterministic automaton that simulates the movement logic of a robot in a 2D matrix of 10 blocks. The automaton is implemented in Python and uses a set of instructions including movements ('MOV') and turns ('TURN') with angles of 90°, 180°, 270°, and 360°. Additionally, error handling has been incorporated to return an illegal instruction message when the movement leads the robot outside the boundaries of the matrix.

The automaton is represented using a directed graph using the Graphviz library, allowing for a clear visualization of the different states and transitions between them. Furthermore, a method is included to execute a sequence of instructions and determine if they have been successfully completed or if there are missing instructions.

This project provides a basic implementation of the automaton and can be customized and expanded upon to meet specific needs. It is useful for understanding automaton concepts and movement logic in the context of a robot in a 2D matrix.

<p align="center">
<img width="449" alt="Captura de pantalla 2023-05-31 a la(s) 14 28 59" src="https://github.com/Neuvax/ProjectRobin/assets/114161329/c8e0d4c8-3101-4f86-a8c8-29ee13d550fe">
</p>
  
## CPU Program

This program is a simple simulation of a robot's movement on a 10x10 grid. It reads a set of instructions from a file and executes them to move the robot within the grid.

Let's go through the main components and their functionalities:

**Variables:**

**robot_x** and **robot_y** represent the current position of the robot on the grid.
direction represents the current direction the robot is facing **(->, ↑, <-, ↓)**.
rotation_angle keeps track of the rotation angle of the robot.
field is a 2D list that represents the grid where the robot moves.
**clear_field()**: This function resets the grid by filling it with dashes ("-").

**plot()**: This function prints the current state of the grid, including the robot's position and direction.

**turn(angle)**: This function updates the rotation_angle and direction based on the given angle. The **rotation_angle** is adjusted modulo 360 to keep it within the range of 0 to 359 degrees, with valid angles like 0, 90, 180 and 270. The direction is updated based on the **rotation_angle**.

**move(blocks)**: This function moves the robot a certain number of blocks in the current direction. It checks if the movement will be within the grid boundaries before updating the **robot_x** and **robot_y** coordinates. After each movement, the grid is cleared, and the updated state is plotted.

**execute_actions_from_file(file_path)**: This function reads a file line by line and performs the corresponding action based on the instruction. If the action is **"MOV"**, it calls the move() function with the specified value. If the action is **"TURN"**, it calls the **turn()** function with the specified value. Any other action is considered invalid.

**main()**: This function initializes the grid by calling **plot()** and then calls **execute_actions_from_file()** with the given file path.

The program reads instructions from a file, which include movement and rotation commands. It simulates the robot's movement on a grid and displays the resulting state at each step. This program can be used to demonstrate and visualize how a robot navigates and moves within a given environment.
