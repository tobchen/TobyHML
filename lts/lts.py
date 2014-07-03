class LTS:

    """An LTS (Labeled Transition System) class."""

    def __init__(self):
        self.states = []

    def add_state(self, state_name):
        state_found = False
        for state in self.states:
            if state.name == state_name:
                state_found = True
                break
        if not state_found:
            self.states.append(self.State(state_name))

    def add_transition(self, state_from, transition, state_to):
        self.add_state(state_from)
        self.add_state(state_to)
        for state in self.states:
            if state.name == state_from:
                state.add_transition(transition, state_to)
                break

    def remove_state(self, state_name):
        pass  # TODO implement

    def remove_transition(self, state_from, transition, state_to):
        pass  # TODO implement

    def reset(self):
        self.states.clear()

    def __str__(self):
        result = ''
        divider = ''
        for state in self.states:
            result += (divider + str(state))
            divider = '\n'
        return result

    class State:
        def __init__(self, name):
            self.name = name
            self.transitions = []

        def add_transition(self, name, to_state):
            transition_found = False
            for transition in self.transitions:
                if transition.name == name:
                    transition.add_to_state(to_state)
                    transition_found = True
                    break
            if not transition_found:
                self.transitions.append(self.Transition(name, to_state))

        def __str__(self):
            result = self.name
            for transition in self.transitions:
                result += ('\n\t' + str(transition))
            return result

        class Transition:
            def __init__(self, name, to_state=None):
                self.name = name
                self.to_states = []
                if to_state is not None:
                    self.to_states.append(to_state)

            def add_to_state(self, to_state):
                to_found = False
                for to in self.to_states:
                    if to == to_state:
                        to_found = True
                        break
                if not to_found:
                    self.to_states.append(to_state)

            def __str__(self):
                return self.name + " -> " + str(self.to_states)