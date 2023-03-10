
### EX04 PYTHON ###

pop_a = 80000
pop_b = 200000
cresc_a = 0.03
cresc_b = 0.015

ano = 0

while pop_a < pop_b:
    pop_a = pop_a + (pop_a*cresc_a)
    pop_b = pop_b + (pop_b*cresc_b)
    ano += 1
    print("ANO: {}".format(ano))
    print("POP_A: {:.2f} \nPOP_B: {:.2f}".format(pop_a, pop_b))
    print('-' * 10)

print(ano)
