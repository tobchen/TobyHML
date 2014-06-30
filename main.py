__author__ = 'Tobias Heukaeufer'

from cmd import Cmd
from hmltoby.parse import ParseException, parse
from hmltoby.evaluate import evaluate
from lts.lts import LTS


lts = LTS()


class HMLTobyPrompt(Cmd):

    """Commandline interface for TobyHML."""

    intro = 'Welcome to TobyHML!'
    prompt = '> '

    def help_add(self):
        """Help-text for 'add'."""
        print('Adds a new state or transition.')
        print('Use "add <state>" to add a state or "add <from_state>', end='')
        print('<transition> <to_state>" to add a transition.')

    def help_evaluate(self):
        """Help-text for 'evaluate'."""
        print('Returns states that meet a given HML formula.')
        print('HML-syntax used: F := true | false | (F and F) |', end='')
        print('(F or F) | <a>F | [a]F')
        print('Examples: "evaluate <a><b>true", "evaluate (<a>true or <b>true)"')

    def do_add(self, line):
        """Add a new state or transition."""
        args = line.split()

        valid_input = True
        for argument in args:
            valid_input = valid_input\
                and HMLTobyPrompt.is_input_valid(argument)

        if valid_input:
            # Add state
            if len(args) == 1:
                lts.add_state(args[0])
                print('Added ' + args[0])
            # Add transition (and possibly states)
            elif len(args) >= 3:
                lts.add_transition(args[0], args[1], args[2])
                print('Added ' + args[0] + ' -' + args[1] + '-> ' + args[2])
        else:
            print('Invalid input!')
            print('Input must be alphanumeric', end='')
            print(', may not be true, false, or, and!')

    def do_reset(self, _):
        """Reset current LTS. Removes all states and transitions."""
        lts.reset()
        print('LTS has been reset!')

    def do_evaluate(self, line):
        """Return states that meet a given HML formula."""
        try:
            start_token = parse(line)
            the_set = evaluate(start_token, lts)
            # TODO Beautiful output
            print(the_set)
        except IndexError:
            print('Bad syntax!')
        except ParseException as e:
            print(e.value)

    def do_exit(self, _):
        """Exit TobyHML."""
        return True

    def do_print(self, _):
        """Print current LTS on screen."""
        print(lts)

    def do_about(self, _):
        """About TobyHML."""
        print('TobyHML by Tobias Heukäufer')
        print('- Yes, he named the program after himself.')

    def is_input_valid(self, name):
        """Check if an input is alphanumeric, not true, false, and, or."""
        lowered = name.lower()
        return lowered.isalnum() and lowered != 'true' and lowered != 'false'\
            and lowered != 'and' and lowered != 'or'

if __name__ == '__main__':
    HMLTobyPrompt().cmdloop()