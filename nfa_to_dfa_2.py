# Reference https://pypi.org/project/fsmdot/

from fsmdot.nfa import Nfa


Q = {'A','B', 'C', 'D'}
S = {'0', '1'}
d = {
    'A': {
        '0': {'A','B'},
        '1': {'A'}
    },
    'B': {
        '0': {'C'},
        '1': {'C'}
    },
    'C': {
        '0': {'D'},
        '1': {'D'}
    },
    'D': {
    }
}
q0 = 'A'
F = {'D'}

a = Nfa(Q, S, d, q0, F)
a.print_table()

G = a.dot_graph()
G.write('nfa_table.dot')

# Conversion to DFA
dfa = a.to_dfa()
dfa.print_table()
G2 = dfa.dot_graph()
G2.write('dfa_table.dot')