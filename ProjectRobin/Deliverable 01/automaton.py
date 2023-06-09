import graphviz

class RobotAutomaton:
    def __init__(self):
        self.states = {
            'iS': {'MOV, x': 'MOV( )', 'TURN, x': 'TURN( )'},
            'MOV( )': {'ϵ': 'fS'},
            'TURN( )': {'ϵ': 'fS'},
            'fS': {'MOV, x': 'MOV( )', 'TURN, x': 'TURN( )', 'OoR': 'Error'}
        }
        self.current_state = 'iS'

    def process_instruction(self, instruction):
        if instruction not in self.states[self.current_state]:
            return "Illegal instruction error"
        else:
            self.current_state = self.states[self.current_state][instruction]
            return ""

    def run(self, instructions):
        for instruction in instructions:
            result = self.process_instruction(instruction)
            if result != "":
                return result
        if self.current_state == 'fS':
            return "Instructions executed successfully"
        else:
            return "Incomplete instructions"

    def draw_automaton(self):
        dot = graphviz.Digraph()
        for state in self.states:
            if state == 'fS':
                dot.node(state, state, shape='doublecircle')
            else:
                dot.node(state, state)
        for state, transitions in self.states.items():
            for symbol, next_state in transitions.items():
                dot.edge(state, next_state, label=symbol)
        dot.render('robot_automaton.gv', view=True)

robot = RobotAutomaton()

instructions = 'MOV, 2'.split()
result = robot.run(instructions)
print(result)

robot.draw_automaton()