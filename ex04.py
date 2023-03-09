
### EX01 PYTHON ###

pop_a = 80000
pop_b = 200000
cresc_a = 0.03
cresc_b = 0.015

ano = 1

while pop_a < pop_b:
    pop_a = pop_a + (pop_a*cresc_a)
    pop_b = pop_b + (pop_b*cresc_b)

