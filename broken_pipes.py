from dwave.system import DWaveSampler, EmbeddingComposite

sampler = EmbeddingComposite(DWaveSampler())

# QUBO = A + 2B - C - D + F + 2DC + 2CE - 2AB - 2BC - 2FG - 2GE - 4
linear = {('a', 'a'): 1, ('b', 'b'): 2, ('d', 'd'): -1, ('f', 'f'): 1, ('g', 'g'): 2, ('c', 'c'): -1}
quadratic = {('a', 'b'): -2, ('b', 'c'): -2, ('d', 'c'): 2, ('c', 'e'): 2, ('f', 'g'): -2, ('g', 'e'): -2}
Q = {**linear, **quadratic}

sampleset = sampler.sample_qubo(Q, num_reads=5000)

print(sampleset)