import numpy as np

# estabelecemos qual a probabilidade que usaremos na simulacao
PROB = 0.6

# numero de simulacoes a serem realizadas
N_SIMULATIONS = 10000

# contador de quantas vezes saiu cara
count_head = 0

# Lista com as saídas da moeda (Cara:1, Coroa:0)
simul_output = []

for i in range(0, N_SIMULATIONS):
    if (np.random.uniform() < PROB):
        count_head += 1
        simul_output.append(1)
    else:
        simul_output.append(0)

print('Jogadas:', simul_output)
print('Frequencia de caras:', count_head/N_SIMULATIONS)