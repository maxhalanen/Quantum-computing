The code is copied and slightly modified from https://docs.dwavesys.com/docs/latest/c_gs_8.html

Just playing around with it to see what other examples I can formulate

The objective for this model is: Given a system of broken and functioning pipes, locate
the functioning connections and broken connections.

If adjacent joints in the system are the same number the pipe connecting them is working, 
otherwise it is broken.

It does not work with every system of pipes, if there is a system that cannot be represented with binary, it wont work.


How i made the QUBO:

Working pipe connection truth table:
q1 q2  f(q1, q2)
0  0  -1
0  1   0
1  0   0
1  1  -1

f(q1, q2) = q1 + q2 - 2q1q2 - 1

broken pipe connection truth table:
q1 q2  b(q1, q2)
0  0   0
0  1  -1
1  0  -1
1  1   0

b(q1, q2) = -q1 -q2 + 2q1q2

Substitute the qubits (q1, q2) for the connections (A,B,C,D,E,F)

adding every connection for our pipe layout gives the QUBO
QUBO = A + 2B - C - D + F + 2DC + 2CE - 2AB - 2BC - 2FG - 2GE - 4